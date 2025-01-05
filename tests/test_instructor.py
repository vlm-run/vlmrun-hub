import os
from typing import Type

import pytest
from loguru import logger
from pydantic import BaseModel

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


@pytest.mark.benchmark
def test_instructor_hub_dataset(instructor_client):
    from vlmrun.hub.dataset import VLMRUN_HUB_DATASET
    from vlmrun.hub.utils import encode_image

    for sample in VLMRUN_HUB_DATASET.values():
        logger.debug(f"Testing domain={sample.domain}, sample={sample}")
        logger.debug(f"sample.image={sample.image}")
        response_model: Type[BaseModel] = sample.response_model
        response = instructor_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": sample.prompt},
                        *[
                            {"type": "image_url", "image_url": {"url": encode_image(img, format="JPEG")}}
                            for img in [sample.image,]
                        ],
                    ],
                },
            ],
            response_model=response_model,
            temperature=0,
        )
        logger.info(response.model_dump_json(indent=2))
