import os
from typing import List, Optional, Type

import pytest
from loguru import logger
from pydantic import BaseModel

pytestmark = pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY", False), reason="This test requires OPENAI_API_KEY to be set"
)


@pytest.fixture
def openai_client():
    from openai import OpenAI

    return OpenAI()


def test_openai_structured_outputs_simple(openai_client):
    from pydantic import Field

    from vlmrun.common.image import encode_image
    from vlmrun.common.utils import remote_image

    invoice_url = "https://storage.googleapis.com/vlm-data-public-prod/hub/examples/document.invoice/invoice_1.jpg"
    invoice_image = remote_image(invoice_url)

    class Address(BaseModel):
        street: Optional[str] = Field(None, description="Street address")
        city: Optional[str] = Field(None, description="City")
        state: Optional[str] = Field(None, description="State")
        postal_code: Optional[str] = Field(None, description="Postal code")
        country: Optional[str] = Field(None, description="Country")

    class Item(BaseModel):
        description: Optional[str] = Field(None, description="Description or name of the item")
        quantity: Optional[int] = Field(None, description="Quantity of the item")
        currency: Optional[str] = Field(None, description="3-digit currency code")
        unit_price: Optional[float] = Field(None, description="Unit price of the item")
        total_price: Optional[float] = Field(None, description="Total price of the item")

    class Invoice(BaseModel):
        invoice_id: Optional[str] = Field(None, description="Unique invoice identifier")
        invoice_issue_date: Optional[str] = Field(None, description="Issue date of the invoice")

        customer_billing_address: Optional[Address] = Field(None, description="Recipient's billing address")
        customer_shipping_address: Optional[Address] = Field(None, description="Recipient's shipping address")

        items: Optional[List[Item]] = Field(None, description="Items in the invoice")
        subtotal: Optional[float] = Field(None, description="Subtotal of the invoice")
        tax: Optional[float] = Field(None, description="Tax of the invoice")
        total: Optional[float] = Field(None, description="Total of the invoice")
        currency: Optional[str] = Field(None, description="Currency of the invoice")

    response = openai_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Extract the invoice in JSON."},
                    *[
                        {"type": "image_url", "image_url": {"url": encode_image(img, format="JPEG")}}
                        for img in [invoice_image]
                    ],
                ],
            },
        ],
        response_format=Invoice,
        temperature=0,
    )
    logger.info(response.choices[0].message.parsed.model_dump_json(indent=2))


@pytest.mark.benchmark
@pytest.mark.skip(reason="This test is not working due to the patch_response_format function")
def test_openai_structured_outputs_hub_dataset(openai_client):
    from vlmrun.common.image import encode_image
    from vlmrun.hub.dataset import VLMRUN_HUB_DATASET
    from vlmrun.hub.utils import patch_response_format

    for sample in VLMRUN_HUB_DATASET.values():
        response_model: Type[BaseModel] = sample.response_model
        response = openai_client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": sample.prompt},
                        *[
                            {"type": "image_url", "image_url": {"url": encode_image(img, format="JPEG")}}
                            for img in [
                                sample.image,
                            ]
                        ],
                    ],
                },
            ],
            response_format=patch_response_format(response_model),
            temperature=0,
        )
        logger.info(response.model_dump_json(indent=2))
