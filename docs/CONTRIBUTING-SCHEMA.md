# Contributing Schemas to VLM Run Hub

Thank you for your interest in contributing schemas to the VLM Run Hub! To ensure consistency and quality, please follow these guidelines.

## Guidelines for Writing a Schema

Please refer to the [Schema Guidelines](./SCHEMA-GUIDELINES.md) for comprehensive instructions on creating schemas. Key points include:

- **Use Pydantic’s BaseModel**: All schemas should inherit from Pydantic’s `BaseModel`.
- **Strongly-Typed Fields**: Ensure all fields are strongly-typed with precise annotations.
- **Field Metadata**: Include descriptions and constraints for each field.
- **Examples**: Provide example data using `Config.schema_extra`.

## Adding a New Schema

1. **Create a New Schema File**: Place your schema in `schemas/contrib/<industry>/<use_case>.py`, following the appropriate industry and use case structure defined in the [Schema Guidelines](./SCHEMA-GUIDELINES.md).

2. **Add Tests**: Include tests for your schema in `tests/test_schemas.py`.

3. **Add to the contrib Catalog**: Add your schema to the [`vlmrun/hub/schemas/contrib/catalog.yaml`](../vlmrun/hub/schemas/contrib/catalog.yaml) file in the `schemas` section, and test it with `pytest -sv tests/test_instructor.py --domain="<domain_name>"`.

4. **Submit a Pull Request**: Once your schema is complete and tested, submit a pull request with the [`schema-request`](../.github/PULL_REQUEST_TEMPLATE/schema-request.yaml) template for review. You can take a look at a previous PR for reference.

## PR Checklist

Before submitting your schema, ensure:

- Follow the [Schema Review Checklist](./SCHEMA-GUIDELINES.md#✅-schema-review-checklist)
- Add the schema to the [`vlmrun/hub/schemas/contrib/catalog.yaml`](../vlmrun/hub/schemas/contrib/catalog.yaml) file, following the [Adding a New Schema to the Hub](./SCHEMA-GUIDELINES.md#👩‍💻-adding-a-new-schema-to-the-hub) section
- Make sure the sample image is publicly accessible.
- Test the schema with `pytest -sv tests/test_instructor.py. --domain="<domain_name>"`.

Thank you for helping us maintain high standards for schema contributions!
