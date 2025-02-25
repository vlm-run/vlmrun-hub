import os
from typing import Literal

import pytest
from conftest import BenchmarkResult, create_benchmark
from dotenv import load_dotenv
from loguru import logger

from vlmrun.common.image import encode_image
from vlmrun.hub.dataset import VLMRUN_HUB_DATASET, HubSample

load_dotenv()


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
    # ("openai", "gpt-4o-2024-08-06"),
    # ("openai", "gpt-4o-2024-11-20"),
    # ("openai", "o1-2024-12-17"),
    # ("openai", "o1-mini-2024-09-12"),
    # ("openai", "o3-mini-2025-01-31"),
    # ("gemini", "gemini-2.0-flash-exp"),
    # ("fireworks", "accounts/fireworks/models/llama-v3p2-11b-vision-instruct"),
    # ("ollama", "llama3.2-vision:11b"),
    # ("ollama", "bsahane/Qwen2.5-VL-7B-Instruct:Q4_K_M_benxh"),
]


def test_instructor_hub_sample(provider_arg: str, model_arg: str, domain_arg: str):
    from rich import print

    provider, model, domain = provider_arg, model_arg, domain_arg

    # Get the client (based on provider)
    try:
        instructor_client = get_instructor_client(provider)
    except Exception as e:
        pytest.skip(f"Error getting instructor client: {e}")

    logger.debug(f"Testing provider={provider}, model={model}, domain={domain}")
    sample = VLMRUN_HUB_DATASET[domain]
    logger.debug(f"Testing domain={sample.domain}, sample={sample}")
    logger.debug(f"sample.images={sample.images}")
    response = process_sample(instructor_client, sample, model=model)
    print(response.model_dump_json(indent=2))
    assert response is not None


@pytest.mark.benchmark
@pytest.mark.parametrize("provider_model", PROVIDER_MODELS)
def test_instructor_hub_dataset(provider_model: tuple[str, str]):
    provider, model = provider_model

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
            BenchmarkResult(
                domain=sample.domain,
                sample=sample.data,
                response_model=sample.response_model.__name__,
                response_json=response.model_dump_json(indent=2, exclude_none=False) if response else None,
            )
        )
        if response:
            logger.debug(response.model_dump_json(indent=2))

    create_benchmark(results, model, suffix="instructor")
