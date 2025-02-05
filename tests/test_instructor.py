import os
from typing import Literal

import pytest
from loguru import logger

from vlmrun.common.image import encode_image
from vlmrun.hub.dataset import VLMRUN_HUB_DATASET, HubSample


def get_instructor_client(provider: Literal["openai", "gemini", "fireworks", "ollama"] = "openai"):
    import instructor
    from openai import OpenAI

    client = None
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY", None)
        if not api_key:
            raise ValueError("OPENAI_API_KEY is not set")
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.openai.com/v1",
        )
    elif provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY", None)
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not set")
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
    elif provider == "fireworks":
        api_key = os.getenv("FIREWORKS_API_KEY", None)
        if not api_key:
            raise ValueError("FIREWORKS_API_KEY is not set")
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.fireworks.ai/inference/v1",
        )
    elif provider == "ollama":
        client = OpenAI(
            api_key="ollama",
            base_url="http://localhost:11434/v1/",
        )
        client.models.list()  # check if ollama is running, otherwise raise an error
    else:
        raise ValueError(f"Invalid provider: {provider}")

    return instructor.from_openai(
        client,
        mode=instructor.Mode.MD_JSON,
    )


def process_sample(client, sample: HubSample, model: str):
    return client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": sample.prompt},
                    *[
                        {"type": "image_url", "image_url": {"url": encode_image(img, format="JPEG")}}
                        for img in sample.images
                    ],
                ],
            },
        ],
        response_model=sample.response_model,
        temperature=0,
        max_retries=0,
    )


PROVIDER_MODELS = [
    ("openai", "gpt-4o-mini-2024-07-18"),
    ("openai", "gpt-4o-2024-11-20"),
    ("gemini", "gemini-2.0-flash-exp"),
    ("fireworks", "accounts/fireworks/models/llama-v3p2-11b-vision-instruct"),
    ("ollama", "llama3.2-vision:11b"),
]


@pytest.mark.parametrize("provider_model", PROVIDER_MODELS[:1])
def test_instructor_hub_sample(provider_model: tuple[str, str], domain_arg: str):
    provider, model = provider_model

    # Get the client (based on provider)
    try:
        instructor_client = get_instructor_client(provider)
    except Exception as e:
        pytest.skip(f"Error getting instructor client: {e}")

    logger.debug(f"Testing provider={provider}, model={model}")
    sample = VLMRUN_HUB_DATASET[domain_arg]
    logger.debug(f"Testing domain={sample.domain}, sample={sample}")
    logger.debug(f"sample.images={sample.images}")
    response = process_sample(instructor_client, sample, model=model)
    logger.debug(response.model_dump_json(indent=2))
    assert response is not None


@pytest.mark.benchmark
@pytest.mark.parametrize("provider_model", PROVIDER_MODELS)
def test_instructor_hub_dataset(provider_model: tuple[str, str]):
    provider, model = provider_model
    from datetime import datetime
    from pathlib import Path

    # Get the client (based on provider)
    try:
        instructor_client = get_instructor_client(provider)
    except Exception as e:
        pytest.skip(f"Error getting instructor client: {e}")

    # Process all samples
    results = []
    for sample in VLMRUN_HUB_DATASET.values():
        logger.debug(f"Testing domain={sample.domain}, sample={sample}")
        logger.debug(f"sample.images={sample.images}")

        # Try to process the sample
        try:
            response = process_sample(instructor_client, sample, model=model)
        except Exception as e:
            response = None
            logger.error(f"Error processing sample {sample.domain}: {e}")

        results.append(
            {
                "domain": sample.domain,
                "sample": sample.data,
                "response_model": sample.response_model.__name__,
                "response_json": response.model_dump_json(indent=2) if response else None,
            }
        )
        if response:
            logger.debug(response.model_dump_json(indent=2))

    # Write the results to a pandas dataframe -> HTML
    # render the data_url in a new column
    BENCHMARK_DIR = Path(__file__).parent / "benchmarks"
    BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    benchmark_path = BENCHMARK_DIR / f"{date_str}-{model}-instructor-results.md".replace("/", "-")

    # Render the results in markdown
    def parse_json(x):
        return x.replace("\n", "<br>") if x is not None else "❌"

    markdown_str = f"## Benchmark Results (model={model}, date={date_str})\n\n"
    markdown_str += """<table>
<tr>
<td style='width: 5%;'> Domain </td>
<td style='width: 5%;'> Response Model </td>
<td style='width: 40%;'> Sample </td>
<td style='width: 50%;'> Response JSON </td>
</tr>
    """
    for result in results:
        markdown_str += "<tr>"
        markdown_str += f"<td> <kbd>{result['domain']}</kbd> </td>\n"
        markdown_str += f"<td> <kbd>{result['response_model']}</kbd> </td>\n"
        markdown_str += f"<td> <img src='{result['sample']}' width='100%' /> </td>\n"
        markdown_str += "<td> <pre>{x}</pre> </td>\n".format(x=parse_json(result["response_json"]))
        markdown_str += "</tr>"
    markdown_str += "\n</table>"

    with benchmark_path.open("w") as f:
        f.write(markdown_str)
    logger.debug(f"Results written to {benchmark_path}")
