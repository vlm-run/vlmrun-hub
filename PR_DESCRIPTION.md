# Add retail.ecommerce-product-caption schema

This PR introduces a new schema `retail.ecommerce-product-caption` based on the existing `web_ecommerce_product_catalog` model. The new schema uses primitive types only and includes the specified sample image data.

## Sample Image
![Kindle Paperwhite](https://storage.googleapis.com/vlm-data-public-prod/hub/examples/retail.ecommerce-product-caption/Electronics%20-%20Kindle.webp)

## Changes
- Added new domain ID `retail_ecommerce_product_caption`
- Created retail package with __init__.py and schema
- Implemented RetailEcommerceProductCaption schema using primitive types
- Added field validation constraints (rating: 0-100)
- Removed duplicate schema from contrib/retail
- Removed Config class for simplicity
- Reverted test model references to gpt-4o-mini-2024-07-18

## Testing Status
Test execution is blocked by:
1. Required OPENAI_API_KEY environment variable
2. Using custom model "gpt-4o-mini-2024-07-18"
Awaiting access to required model and API key.

Link to Devin run: https://app.devin.ai/sessions/85a9408ec3cf45838df4f59bf1084c07
