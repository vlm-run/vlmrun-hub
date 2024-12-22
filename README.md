## VLM Run Hub

Welcome to **VLM Run Hub**, the ultimate repository of pre-defined [Pydantic](https://docs.pydantic.dev/latest/) schemas for extracting structured data from unstructured visual domains such as images, videos, and documents. Powered by [Vision Language Models (VLMs)](https://huggingface.co/blog/vlms) and optimized for real-world use cases, VLM Run Hub simplifies the integration of visual ETL into your workflows.


<p align="center">
<a href="https://vlm.run"><b>Website</b></a> | <a href="https://docs.vlm.run/"><b>Docs</b></a> | <a href="https://docs.vlm.run/blog"><b>Blog</b></a> | <a href="https://discord.gg/4jgyECY4rq"><b>Discord</b></a>
</p>
<p align="center">
<a href="https://pypi.org/project/vlmrun-hub/"><img alt="PyPI Version" src="https://badge.fury.io/py/vlmrun-hub.svg"></a>
<a href="https://pypi.org/project/vlmrun-hub/"><img alt="PyPI Version" src="https://img.shields.io/pypi/pyversions/vlmrun-hub"></a>
<a href="https://www.pepy.tech/projects/vlmrun-hub"><img alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/vlmrun-hub"></a>
<a href="https://github.com/vlm-run/vlmrun-hub/blob/main/LICENSE"><img alt="PyPi Downloads" src="https://img.shields.io/github/license/vlm-run/hub.svg"></a>
<a href="https://discord.gg/4jgyECY4rq"><img alt="Discord" src="https://img.shields.io/badge/discord-chat-purple?color=%235765F2&label=discord&logo=discord"></a>
<a href="https://twitter.com/vlmrun"><img alt="PyPi Version" src="https://img.shields.io/twitter/follow/vlmrun.svg?style=social&logo=twitter"></a>
</p>

## 💡 Motivation

While foundation vision models like OpenAI’s [GPT-4o](https://openai.com/index/hello-gpt-4o/) and Anthropic’s [Claude Vision](https://www.anthropic.com/claude) offer impressive capabilities such as question answering over visual inputs (i.e., "chat with images"), they often fall short in practical software workflows. Chat-based interfaces excel in exploratory tasks but are not ideal for automation or integration into existing systems, where developers need **strongly-typed**, **validated outputs** for seamless functionality.

**Structured Outputs API** (popularized by [GPT-4](https://openai.com/index/introducing-structured-outputs-in-the-api/), [Gemini](https://ai.google.dev/gemini-api/docs/structured-output)) is built on exactly this insight - instead of free-form text outputs, LLMs can be constrained to return data in precise, strongly-typed formats that are immediately usable in production systems. By defining strict JSON schemas, developers can ensure that model outputs conform to expected types and structures, eliminating the need for complex parsing and validation logic.

The schemas defined can be arbitrarily nested, and can include lists, dictionaries, and other complex types that can richly capture the information contained in the input. This enables seamless integration with existing type systems and data models in your codebase, while maintaining the full analytical and reasoning capabilities of the underlying model.

### Why use this repo / pre-defined Pydantic schemas?

- 📚 **Easy to use:** Pydantic is a well-understood and battle-tested data model for structured data.
- 🔋 **Batteries included:**  Each schema in this repo has been validated across real-world industry use cases—from healthcare to finance to media—saving you weeks of development effort.
- 🔍 **Automatic Data-validation:** Built-in [Pydantic](https://docs.pydantic.dev/latest/) validation ensures your extracted data is clean, accurate, and reliable, reducing errors and simplifying downstream workflows.
- 🔌 **Type-safety:** With [Pydantic’s](https://docs.pydantic.dev/latest/) type-safety and compatibility with tools like `mypy` and `pyright`, you can build composable, modular systems that are robust and maintainable.
- 🧰 **Model-agnostic:** Use the same schema with multiple VLM providers, no need to rewrite prompts for different VLMs.
- 🚀 **Optimized for Visual ETL:** Purpose-built for extracting structured data from images, videos, and documents, this repo bridges the gap between unstructured data and actionable insights.


## 🚀 Getting Started

Let's say we want to extract invoice metadata from an [invoice image](https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg). You can readily use our `Invoice` schema we have defined under `vlmrun.hub.schemas.document.invoice` and use it with any VLM of your choosing.

### With OpenAI / [Instructor](https://github.com/jxnl/instructor)

```python
import instructor
from openai import OpenAI

from vlmrun.hub.schemas.document.invoice import Invoice

IMAGE_URL = "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg"

client = instructor.from_openai(
    OpenAI(), mode=instructor.Mode.MD_JSON
)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "user", "content": [
            {"type": "text", "text": "Extract the invoice in JSON."},
            {"type": "image_url", "image_url": {"url": IMAGE_URL}, "detail": "auto"}
        ]}
    ],
    response_model=Invoice,
    temperature=0,
)
```

### With [VLM Run](https://vlm.run)

```python
import requests

from vlmrun.hub.schemas.document.invoice import Invoice


IMAGE_URL = "https://mintlify.s3.us-west-1.amazonaws.com/autonomiai/guides/doc-ai/images/sample-invoice.jpg"
VLM_API_KEY = "<your-api-key>"

json_data = {
    "image": IMAGE_URL,
    "model": "vlm-1",
    "domain": "document.invoice",
    "prompt": "Extract the invoice in JSON.",
    "json_schema": Invoice.model_json_schema(),
}
response = requests.post(
    f"https://api.vlm.run/v1/image/generate",
    headers={"Authorization": f"Bearer {VLM_API_KEY}"},
    json=json_data,
)
```

### Locally with [Ollama](https://ollama.com)

```python
from ollama import chat

from vlmrun.hub.schemas.document.invoice import Invoice
from vlmrun.hub.utils import encode_image

chat_response = chat(
    model="llama3.2-vision:11b",
    format=Invoice.model_json_schema(),
    messages=[
        {
            "role": "user",
            "content": "Extract the invoice in JSON.",
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
response = response_model.model_validate_json(
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
