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

3. **Submit a Pull Request**: Once your schema is complete and tested, submit a pull request for review.

## Review Checklist

Before submitting your schema, ensure:

- All fields are strongly-typed and include metadata.
- Examples are provided in `Config.schema_extra`.
- Custom validators are added for domain-specific rules.
- Tests are included to validate the schema.

Thank you for helping us maintain high standards for schema contributions!
