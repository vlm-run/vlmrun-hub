import requests
import os
from loguru import logger
import json

from dotenv import load_dotenv

from vlmrun.hub.schemas.document.invoice import Invoice
from vlmrun.hub.utils import encode_image, remote_image

load_dotenv()

VLM_API_URL = os.getenv("VLM_API_URL")
VLM_API_KEY = os.getenv("VLM_API_KEY")


def test_vlmrun_invoice():
    invoice_url = "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg"
    invoice_image = remote_image(invoice_url)
    domain = "document.invoice"

    json_data = {
        "file_id": invoice_url,
        "image": encode_image(invoice_image, format="JPEG"),
        "json_schema": Invoice.model_json_schema(),
        "model": "vlm-1",
        "domain": domain,
    }

    response = requests.post(
        f"{VLM_API_URL}/v1/image/generate",
        json=json_data,
        headers={"Authorization": f"Bearer {VLM_API_KEY}"},
    )
    assert response.status_code == 200, f"Response failed: {response.text}"
    json_response = response.json()
    assert isinstance(json_response, dict), "Expected a dict response"
    assert "response" in json_response, "Failed to fetch 'response' key"
    logger.debug(f"Document: {json.dumps(json_response, indent=2)}")

    invoice_data = json_response["response"]
    invoice = Invoice.model_validate_json(json.dumps(invoice_data))
    logger.debug(invoice)
