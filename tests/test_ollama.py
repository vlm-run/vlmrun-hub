import importlib.util
import pytest
from loguru import logger
from vlmrun.hub.dataset import VLMRUN_HUB_DATASET
from pydantic import BaseModel
from typing import Type


@pytest.mark.skipif(
    not importlib.util.find_spec("ollama"), reason="Ollama is not installed"
)
def test_local_ollama():
    from ollama import chat
    from vlmrun.hub.utils import encode_image

    for sample in VLMRUN_HUB_DATASET.values():
        response_model: Type[BaseModel] = sample.response_model
        chat_response = chat(
            model="llama3.2-vision:11b",
            format=response_model.model_json_schema(),  # Pass in the schema for the response
            messages=[
                {
                    "role": "user",
                    "content": sample.prompt,
                    "images": [
                        encode_image(img, format="JPEG").split(",")[1]
                        for img in sample.images
                    ],
                },
            ],
            options={
                "temperature": 0
            },  # Set temperature to 0 for more deterministic output
        )
        response: Type[BaseModel] = response_model.model_validate_json(
            chat_response.message.content
        )
        logger.info(response.model_dump_json(indent=2))
