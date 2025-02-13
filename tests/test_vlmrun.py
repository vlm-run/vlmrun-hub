import json
import os

import pytest
import requests
from dotenv import load_dotenv
from loguru import logger

from vlmrun.common.image import encode_image
from vlmrun.common.utils import remote_image
from vlmrun.hub.schemas.document.invoice import Invoice

load_dotenv()


VLMRUN_API_KEY = os.getenv("VLMRUN_API_KEY", None)
VLMRUN_BASE_URL = os.getenv("VLMRUN_BASE_URL", None)

pytestmark = pytest.mark.skipif(not VLMRUN_API_KEY, reason="This test requires VLMRUN_API_KEY to be set")


def test_vlmrun_invoice():
    invoice_url = "https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.invoice/invoice_1.jpg"
    invoice_image = remote_image(invoice_url)
    domain = "document.invoice"

    json_data = {
        "file_id": invoice_url,
        "images": [encode_image(invoice_image, format="JPEG")],
        "json_schema": Invoice.model_json_schema(),
        "model": "vlm-1",
        "domain": domain,
    }

    response = requests.post(
        f"{VLMRUN_BASE_URL}/v1/image/generate",
        json=json_data,
        headers={"Authorization": f"Bearer {VLMRUN_API_KEY}"},
    )
    assert response.status_code == 201, f"Response failed: {response.text}"
    json_response = response.json()
    assert isinstance(json_response, dict), "Expected a dict response"
    assert "response" in json_response, "Failed to fetch 'response' key"
    logger.debug(f"Document: {json.dumps(json_response, indent=2)}")

    invoice_data = json_response["response"]
    invoice = Invoice.model_validate_json(json.dumps(invoice_data))
    logger.debug(invoice)
