import importlib.util
import pytest
from loguru import logger
from vlmrun.hub.schemas.document.invoice import Invoice



@pytest.mark.skipif(
    not importlib.util.find_spec("ollama"), reason="Ollama is not installed"
)
def test_local_ollama():
    from ollama import chat
    from vlmrun.hub.utils import encode_image, remote_image

    image_urls = [
        "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg",
    ]
    images = [remote_image(url) for url in image_urls]
    chat_response = chat(
        model="llama3.2-vision:11b",
        format=Invoice.model_json_schema(),  # Pass in the schema for the response
        messages=[
            {
                "role": "user",
                "content": "Extract the invoice in JSON format. If you cannot determine certain details, leave those fields empty.",
                "images": [
                    encode_image(img, format="JPEG").split(",")[1] for img in images
                ],
            },
        ],
        options={
            "temperature": 0
        },  # Set temperature to 0 for more deterministic output
    )
    response: Invoice = Invoice.model_validate_json(chat_response.message.content)
    logger.info(response.model_dump_json(indent=2))
