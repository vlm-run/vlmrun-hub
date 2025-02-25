import importlib.util
import os
from typing import Type
from pathlib import Path

import pytest
import requests
from conftest import BenchmarkResult, create_benchmark
from dotenv import load_dotenv
from loguru import logger
from pydantic import BaseModel

from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")


@pytest.mark.skipif(not importlib.util.find_spec("ollama"), reason="Ollama is not installed")
def test_local_ollama():
    from ollama import chat

    from vlmrun.common.image import encode_image

    try:
        requests.get(f"{OLLAMA_BASE_URL}/api/version")
    except requests.exceptions.ConnectionError:
        pytest.skip("Ollama server is not running")

    results = []
    # model = "bsahane/Qwen2.5-VL-7B-Instruct:Q4_K_M_benxh"  # "llama3.2-vision:11b",
    model = "llava"  # "llama3.2-vision:11b",
    samples = [sample for sample in VLMRUN_HUB_DATASET.values() if sample.domain == "healthcare.hipaa-release"]
    # for sample in VLMRUN_HUB_DATASET.values():
    for sample in samples:
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

'''
def test_local_ollama_hipaa():
    from ollama import chat
    from vlmrun.common.image import encode_image
    from vlmrun.hub.schemas.healthcare.hipaa_release import HIPAARelease
    from vlmrun.common.pdf import pdf_images

    # Use local file path instead of downloading
    pdf_path = Path("/Users/scottloftin/Downloads/HIPAA-Journal-sample-HIPAA-release-form-v1-filled.pdf")
    
    # Now pass the Path object to pdf_images
    images = list(pdf_images(pdf_path))
    domain = "healthcare.hipaa-release"
    
    messages = [
        {
            "role": "system",
            "content": "You are a detail-oriented healthcare document analyst. Extract all the relevant information from the HIPAA release form as accurately as possible. You must respond with valid JSON that matches the HIPAARelease schema."
        },
        {
            "role": "user",
            "content": "Please extract the information from this HIPAA release form and return it as JSON with the following fields: patient_name, date_of_birth, address, phone_number, email, healthcare_provider, information_to_release, purpose_of_release, expiration_date, signature_date.",
            "images": [encode_image(images[0].image, format="JPEG").split(",")[1]],
        }
    ]

    # Make the request to Ollama
    try:
        response = chat(
            model="llava",  # or your preferred Ollama model that supports vision
            messages=messages
        )

        import pdb; pdb.set_trace()
        
        # Parse the response into our schema
        result = HIPAARelease.model_validate_json(response.message.content)
        
        # Log the result
        logger.info(f"Extracted HIPAA Release Form Data: {result.model_dump_json(indent=2)}")
        
        # Basic validation
        assert result.patient_name is not None, "Patient name should be extracted"
        assert len(result.authorized_recipients) > 0, "Should have at least one authorized recipient"
        
    except Exception as e:
        logger.error(f"Error processing HIPAA release form: {str(e)}")
        raise
'''
