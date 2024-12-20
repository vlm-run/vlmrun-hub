# VLM Run Hub

Structured extraction for VLMs.

This is a repository of schemas for structured ETL on *visual* domains including:

- **Documents**: PDF, Word, Excel, etc.
- **Images**: JPG, PNG, etc.
- **Videos**: coming soon!

## What is a schema?

Frontier LLM APIs like GPT4, Claude and Gemini now support structured outputs (sometimes referred to as "JSON mode"). While generally
used with text inputs, this approach is particularly powerful for visual data where the goal is to extract information in a
declarative manner.

A schema is a type set of key-value pairs represented as a Pydantic class. Fields can be primitive types or nested TypeClasses and
include a prompt indicating how that field should be populated from the input. They are a data structure that gets filled out
by the VLM per your input and instructions.

Good schemas are a product of 1. good data structure design and 2. good prompts. This repo is meant to be an authoritative source
for both across a variety of inputs, while being agnostic to the VLM provider so it can be used with multiple models.

## How do I run a particular schema on an input?

### With OpenAI/Instructor

```python

from vlmrun.hub.utils import encode_image
from vlmrun.hub.dataset import VLMRUN_HUB_DATASET

import instructor
from openai import OpenAI

from pydantic import BaseModel
from typing import Type


instructor_client = instructor.from_openai(
    OpenAI(),
    mode=instructor.Mode.MD_JSON,
)

image_url = 'YOUR_IMAGE_URL'
response_model: Type[BaseModel] = response_model
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

### Locally

## How is this repo organized?

The hub is organized into a taxonomy of industries and domains, broken down into subcategories for more specific inputs. We hope to expand
to more domains in the near future with the help of the developer community.

## How can I contribute?

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

## Reach out

We'd love to hear from you if you have any questions or feedback!

- [Twitter](https://x.com/vlmrun)
- [Discord](https://discord.gg/vlmrun)
- [Email](mailto:hello@vlmrun.com)
