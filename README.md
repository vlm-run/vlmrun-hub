# VLM Run Hub

Structured extraction for VLMs.

This is a repository of schemas for structured ETL on visual domains including:

📄 Documents
- SEC Filings
- Earnings tables
- Other PDFs

🖼️ Images
- Satellite imagery
- Product images
- Sports

🎥 Videos (coming soon!)

## 💡 Motivation

Frontier LLM APIs like GPT4 and Claude now support structured outputs (usually referred to as "JSON mode") in addition
to the more familiar chat interface. This is particularly powerful for visual data (especially documents) because it allows us to extract information in a declarative manner (i.e. we just list the fields we care about and let the VLM do the rest).

We represent schemas as a Pydantic class of typed key-value pairs. Fields can be primitives (`str`, `int`, etc.) or nested TypeClasses and include a prompt indicating how that field should be populated from the input. In short, they are a data structure that gets filled out by the VLM of your choosing based on your input and instructions.

Good schemas are a product of 1. a good hierarchy of types/fields and 2. good prompts. This repo is meant to be an authoritative source
for both across a variety of input and use-cases, while being agnostic to the VLM provider so it can be used with multiple models.

## 🚀 Usage

### With OpenAI/Instructor

```python
import instructor
from openai import OpenAI
from pydantic import BaseModel
from typing import Type

from vlmrun.hub.utils import encode_image
from vlmrun.hub.schemas.document.invoice import Invoice

instructor_client = instructor.from_openai(
    OpenAI(),
    mode=instructor.Mode.MD_JSON,
)

image_url = 'YOUR_IMAGE_URL'
response_model = Invoice # or any other schema
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
                {
                    "type": "image_url",
                    "image_url": {
                        "url": encode_image(image_url, format="JPEG")
                    },
                    "detail": "auto",
                }
            ],
        },
    ],
    response_model=response_model,
    temperature=0,
)
```

### With VLM Run

```python
import requests

from vlmrun.hub.schemas.document.invoice import Invoice
from vlmrun.hub.utils import encode_image, remote_image

VLM_API_URL = "VLM_API_URL"
VLM_API_KEY = "VLM_API_KEY"

invoice_url = "YOUR_INVOICE_URL"
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
```

### Locally with Ollama

```python
from pydantic import BaseModel
from typing import Type
from ollama import chat

from vlmrun.hub.utils import encode_image
from vlmrun.hub.schemas.document.invoice import Invoice

response_model = Invoice
prompt = "YOUR_PROMPT"

chat_response = chat(
    model="llama3.2-vision:11b",
    format=response_model.model_json_schema(),
    messages=[
        {
            "role": "user",
            "content": prompt,
            "images": [
                encode_image(img, format="JPEG").split(",")[1]
                for img in sample.images
            ],
        },
    ],
    options={
        "temperature": 0
    },
)
response: Type[BaseModel] = response_model.model_validate_json(
    chat_response.message.content
)
```

## How is this repo organized?

The hub is organized into a taxonomy of industries and domains, broken down into subcategories for more specific inputs. We hope to expand
to more domains in the near future with the help of the developer community.

## 🤝 How can I contribute?

We welcome and encourage contributions from the developer community, and we have a few guidelines around writing good schemas:

### Be as specific as possible without being verbose

Be specific about the name, type and prompt for each field. The clearer the relationship between the input and the field, the
better the result tends to be. Prompts should be concise (1-2 sentences) and to the point. Longer prompts can lead to slower
inference times.

### Use nested schemas where appropriate

If a field is a complex object, use a TypeClass to represent it.

### DRY: Don't repeat yourself

Try to place new schemas in the appropriate location and reuse other schemas as subtypes where possible. The goal is to provide a type system
for a variety of visual inputs without needing to duplicate information for similar use cases.

## 📬 Reach out

We'd love to hear from you if you have any questions or feedback!

- [Twitter](https://x.com/vlmrun)
- [Discord](https://discord.gg/nz8QZwTH)
- [Email](mailto:hello@vlmrun.com)
