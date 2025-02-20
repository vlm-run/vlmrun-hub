import importlib.util
import os
from typing import Type

import pytest
import requests
from conftest import BenchmarkResult, create_benchmark
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel

from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


@pytest.mark.benchmark
@pytest.mark.skipif(not importlib.util.find_spec("ollama"), reason="Ollama is not installed")
def test_local_ollama():
    from ollama import chat

    from vlmrun.common.image import encode_image

    try:
        requests.get(f"{OLLAMA_BASE_URL}/api/version")
    except requests.exceptions.ConnectionError:
        pytest.skip("Ollama server is not running")

    results = []
    model = "bsahane/Qwen2.5-VL-7B-Instruct:Q4_K_M_benxh"  # "llama3.2-vision:11b",
    for sample in VLMRUN_HUB_DATASET.values():
        response_model: Type[BaseModel] = sample.response_model
        try:
            chat_response = chat(
                model=model,
                format=response_model.model_json_schema(),  # Pass in the schema for the response
                messages=[
                    {
                        "role": "user",
                        "content": sample.prompt,
                        "images": [encode_image(img, format="JPEG").split(",")[1] for img in sample.images],
                    },
                ],
                options={"temperature": 0},  # Set temperature to 0 for more deterministic output
            )
            response: Type[BaseModel] = response_model.model_validate_json(chat_response.message.content)
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

    create_benchmark(results, model, suffix="ollama")
