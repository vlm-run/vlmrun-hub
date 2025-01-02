# Schema Guidelines

Thank you for contributing to the VLM Run Hub! To maintain consistency and adhere to industry best practices, please follow these guidelines when creating a new schema.


## ✏️ Guidelines for Writing a Schema

1. **Use Pydantic’s BaseModel**: All schemas must inherit from Pydantic’s `BaseModel`.
   ```python
   from pydantic import BaseModel

   class ExampleSchema(BaseModel):
      ...
   ```

2. **Strongly-Typed Fields**: Define each field with precise, strongly-typed annotations (e.g., `str`, `int`, `float`, `list`, `dict`).

3. **Optional Fields**: Use `| None` as the default for optional fields. This is critical as some fields may not be present in the data, and we don't want the Pydantic model to fail the schema validation when this happens.

4. **Descriptive Field Names**: Use clear, descriptive, and `snake_case` field names, along with a short `description` field that explains the field's purpose. This is critical for the model to interpret the field to be mapped from.

   Good example:
   ```python
   class CustomerInvoice(BaseModel):
      invoice_number: str = Field(..., description="The invoice number, typically represented as a string of alphanumeric characters.")
   ```

   Bad example:
   ```python
   class CustomerInvoice(BaseModel):
      invoice_number: str = Field(..., description="The invoice number.")
   ```

5. **Field Metadata**:
   - Use the `Field` class to provide:
     - `default`: If applicable (e.g., `Field(None, ...)`).
     - `description`: Include a short, clear explanation of the field’s purpose. (e.g., `Field(..., description="The invoice number, typically represented as a string of alphanumeric characters.")`)
     - Other constraints: For validation (e.g., `max_length`, `regex`).
     - Validation: Add custom validators where necessary to enforce domain-specific rules.

6. **Nested Models**: Use nested Pydantic models for complex structures (e.g., lists of dictionaries).

   ```python
   class CustomerInvoice(BaseModel):
      invoice_number: str = Field(..., description="The invoice number, typically represented as a string of alphanumeric characters.")
      items: list[Item] = Field(..., description="A list of items in the invoice.")
   ```

7. **Enums**: Use enums or `Literal` for fixed choices.

   Using `Enum`:
   ```python
   class Status(Enum):
      pending = "pending"
      paid = "paid"
      cancelled = "cancelled"

   class CustomerInvoice(BaseModel):
      ...
      status: Status = Field(..., description="The status of the invoice, which can be either 'pending', 'paid', or 'cancelled'.")
   ```

   Using `Literal`:
   ```python
   class CustomerInvoice(BaseModel):
      status: Literal["pending", "paid", "cancelled"] = Field(..., description="The status of the invoice, which can be either 'pending', 'paid', or 'cancelled'.")
   ```

8. **Examples**: Include a `Config.schema_extra` with example data for each schema.

   ```python
   class CustomerInvoice(BaseModel):
      ...

   CustomerInvoice.model_json_schema(indent=2)
   ```

### ✅ Schema Review Checklist

Before submitting your schema:

- [ ] **Field Types**: Ensure all fields are strongly-typed.
- [ ] **Field Metadata**: Check that all fields include descriptions and constraints where applicable.
- [ ] **Examples**: Include clear, complete examples in Config.schema_extra.
- [ ] **Validation**: Add custom validators for domain-specific rules.
- [ ] **Reusability**: Use nested models for complex types and avoid redundancy.
- [ ] **Tests**: Provide unit tests to validate the schema against valid and invalid data.

### 👩‍💻 Adding a New Schema to the Hub

1. **Create a new schema file**: Create a new file in the `schemas/contrib` directory, under the appropriate industry and use case (e.g., `schemas/contrib/retail/ecommerce_product_caption.py`). Follow the [Schema Guidelines](#✏️-guidelines-for-writing-a-schema) to write the schema.

2. **Add sample image, prompt, and test**: Add a sample image, text, or other data that the schema can be applied to and add a pytest test for the schema under `tests/test_schemas.py`.
