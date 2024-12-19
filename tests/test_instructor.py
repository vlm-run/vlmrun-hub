import pytest
from loguru import logger
from vlmrun.hub.schemas.document.invoice import Invoice


@pytest.fixture
def instructor_client():
    import instructor
    from openai import OpenAI

    return instructor.from_openai(
        OpenAI(),
        mode=instructor.Mode.MD_JSON,
    )


def test_instructor(instructor_client):
    from vlmrun.hub.utils import encode_image, remote_image

    image_urls = [
        "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg",
    ]
    images = [remote_image(url) for url in image_urls]
    response = instructor_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Extract the invoice in JSON format. If you cannot determine certain details, leave those fields empty.",
                    },
                    *[
                        {
                            "type": "image_url",
                            "image_url": {"url": encode_image(image, format="JPEG")},
                        }
                        for image in images
                    ],
                ],
            },
        ],
        response_model=Invoice,
        temperature=0,
    )
    logger.info(response.model_dump_json(indent=2))
    
