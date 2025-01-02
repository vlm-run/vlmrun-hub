import os
import pytest
from loguru import logger
from pydantic import BaseModel
from typing import Type


pytestmark = pytest.mark.skipif(not os.getenv("OPENAI_API_KEY", False), reason="This test requires OPENAI_API_KEY to be set")

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
                    "content": sample.prompt,
                    "images": [encode_image(img, format="JPEG").split(",")[1] for img in sample.images],
                },
            ],
            response_model=response_model,
            temperature=0,
        )
        logger.info(response.model_dump_json(indent=2))
