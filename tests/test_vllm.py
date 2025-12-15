import importlib.util
import os
from typing import Type

import PIL.Image
import pytest
import requests
from conftest import BenchmarkResult, create_benchmark
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel
from openai import OpenAI

from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

load_dotenv()

VLLM_BASE_URL = os.getenv("VLLM_BASE_URL", "http://localhost:8000/v1")

@pytest.mark.benchmark
@pytest.mark.skipif(not importlib.util.find_spec("openai"), reason="OpenAI is not installed")
def test_local_vllm():
    from vlmrun.common.image import encode_image
    try:
        requests.get(f"{VLLM_BASE_URL}/health")
    except requests.exceptions.ConnectionError:
        pytest.skip("vLLM server is not running")

    results = []
    model = "bsahane/Qwen2.5-VL-7B-Instruct:Q4_K_M_benxh"

    client = OpenAI(
        base_url=VLLM_BASE_URL,
        api_key="EMPTY",
    )

    for sample in VLMRUN_HUB_DATASET.values():
        response_model: Type[BaseModel] = sample.response_model
        json_schema = response_model.model_json_schema()

        # Convert each image to PIL.Image
        pil_images = []
        for img in sample.images:
            if isinstance(img, PIL.Image.Image):
                pil_images.append(img)
            else:
                pil_images.append(PIL.Image.open(img))
        
        # Create batch input for each image
        for img in pil_images:
            try:
                chat_response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"USER: <image>\n{sample.prompt}\nASSISTANT:"}
                    ],
                    extra_body={"multi_modal_data": {"image": encode_image(img, format="JPEG").split(",")[1]}, "guided_json": json_schema}
                )
                response: Type[BaseModel] = response_model.model_validate_json(chat_response.choices[0].message.content)
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

    create_benchmark(results, model, suffix="vllm")

