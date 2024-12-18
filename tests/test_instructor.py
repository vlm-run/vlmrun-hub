import pytest
from loguru import logger
from pydantic import BaseModel
from typing import Type


@pytest.fixture
def instructor_client():
    import instructor
    from openai import OpenAI

    return instructor.from_openai(
        OpenAI(),
        mode=instructor.Mode.MD_JSON,
    )


def test_instructor(instructor_client):
    from vlmrun.hub.utils import encode_image
    from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

    for sample in VLMRUN_HUB_DATASET.values():
        response_model: Type[BaseModel] = sample.response_model
        response = instructor_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": sample.prompt,
                        },
                        *[
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": encode_image(image, format="JPEG")
                                },
                                "detail": "auto",
                            }
                            for image in sample.images
                        ],
                    ],
                },
            ],
            response_model=response_model,
            temperature=0,
        )
        logger.info(response.model_dump_json(indent=2))
