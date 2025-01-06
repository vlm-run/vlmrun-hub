import os

import pytest
from loguru import logger

from vlmrun.hub.dataset import VLMRUN_HUB_DATASET, HubSample
from vlmrun.hub.utils import encode_image

pytestmark = pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY", False), reason="This test requires OPENAI_API_KEY to be set"
)


@pytest.fixture
def instructor_client():
    import instructor
    from openai import OpenAI

    return instructor.from_openai(
        OpenAI(),
        mode=instructor.Mode.MD_JSON,
    )


def _process_sample(client, sample: HubSample, model: str):
    return client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": sample.prompt},
                    *[
                        {"type": "image_url", "image_url": {"url": encode_image(img, format="JPEG")}}
                        for img in [
                            sample.image,
                        ]
                    ],
                ],
            },
        ],
        response_model=sample.response_model,
        temperature=0,
    )


def test_instructor_hub_sample(instructor_client, domain_arg: str):
    sample = VLMRUN_HUB_DATASET[domain_arg]
    logger.debug(f"Testing domain={sample.domain}, sample={sample}")
    logger.debug(f"sample.image={sample.image}")
    response = _process_sample(instructor_client, sample, model="gpt-4o-mini-2024-07-18")
    logger.debug(response.model_dump_json(indent=2))
    assert response is not None


# @pytest.mark.parametrize("model", ["gpt-4o-mini-2024-07-18", "gpt-4o-2024-11-20"])
@pytest.mark.benchmark
def test_instructor_hub_dataset(instructor_client):
    from datetime import datetime
    from pathlib import Path

    import pandas as pd

    MODEL = "gpt-4o-mini-2024-07-18"

    # Process all samples
    results = []
    for sample in VLMRUN_HUB_DATASET.values():
        logger.debug(f"Testing domain={sample.domain}, sample={sample}")
        logger.debug(f"sample.image={sample.image}")

        # Try to process the sample
        try:
            response = _process_sample(instructor_client, sample, model=MODEL)
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

    # Render the results in a pandas dataframe
    df = pd.DataFrame(results)
    # Render the response_json in a <pre> tag with line breaks
    df["response_json"] = df["response_json"].apply(lambda x: "<pre>{x}</pre>".format(x=x.replace("\n", "<br>")))
    # Render the sample in a <img> tag
    df["sample"] = df["sample"].apply(lambda x: f'<img src="{x}" width="100%" />')
    # Write the results to a pandas dataframe -> HTML
    pd.set_option("display.max_colwidth", 80)
    df.to_html(BENCHMARK_DIR / f"{date_str}-{MODEL}-instructor-results.html", index=False, escape=False)
    logger.debug(f"Results written to {BENCHMARK_DIR / f'{date_str}-{MODEL}-instructor-results.html'}")
