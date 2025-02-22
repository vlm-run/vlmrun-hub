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

3. **Optional Fields**: Use `Optional[...]` to define optional fields. This is critical as some fields may not be present in the document, and we want to make sure that Pydantic data validation does not fail when the JSON returned does not contain the relevant key.

   Example:
   ```python
   class CustomerInvoice(BaseModel):
      invoice_id: str = Field(..., description="The invoice number, typically represented as a string of alphanumeric characters.")
      ...
      invoice_email: Optional[str] = Field(None, description="The email address of the customer, typically represented as a string of alphanumeric characters.")
   ```
   In the example above, the `invoice_email` field is optional as it may or may not be present in the input document. If it is not present in the JSON, the Pydantic model will not fail the schema validation. If the field is present in the JSON, the Pydantic model will validate the field against the schema.

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
- [ ] **Optional Fields**: Use `Optional[...]` to define optional fields.
- [ ] **Examples**: Include clear, complete examples in Config.schema_extra.
- [ ] **Validation**: Add custom validators for domain-specific rules.
- [ ] **Reusability**: Use nested models for complex types and avoid redundancy.
- [ ] **Tests**: Provide unit tests to validate the schema against valid and invalid data.

### 👩‍💻 Adding a New Schema to the Hub

1. **Create a new schema file**: Create a new file in the [`schemas/contrib`](../vlmrun/hub/schemas/contrib) directory, under the appropriate industry and use case (e.g., `schemas/contrib/retail/ecommerce_product_caption.py`). Follow the [Schema Guidelines](#✏️-guidelines-for-writing-a-schema) to write the schema.

2. **Add sample image, prompt and schema reference in `catalog.yaml`:** Add a sample image for the schema, a prompt that can be used with VLMs to appropriately extract the JSON, and a reference to the schema in the [`contrib/catalog.yaml`](../vlmrun/hub/contrib/catalog.yaml) file. You can also refer to the [Catalog Specification Guidelines](./catalog-spec.yaml) for more information on the catalog format.

   Example:
   ```yaml
   - domain: media.nfl-game-state
    schema: vlmrun.hub.schemas.contrib.media.nfl_game_state.NFLGameState
    prompt: "You are a detail-oriented NFL Game Analyst. Extract all the relevant game state information from the video feed or screenshot as accurately as possible."
    description: "NFL game state extraction system that processes game footage or screenshots to extract structured information including teams, scores, game clock, possession, and other relevant game state details."
    sample_data: "https://storage.googleapis.com/vlm-data-public-prod/hub/examples/media.nfl-game-state/packers_cardinals_screenshot.png"
    metadata:
      supported_inputs: ["image", "video"]
      tags: ["media", "sports"]
   ```

3. **Test the schema against the sample data**: Run the following test to ensure the schema is working as expected. Let's say you just added the above schema with `domain=media.nfl-game-state`.

You can run:
```bash
pytest -sv tests/test_instructor.py -k test_instructor_hub_sample --domain media.nfl-game-state
```

This will download the sample data from the URL and call [Instructor](https://github.com/jxnl/instructor/) with `gpt-4o-mini` to generate a JSON output against the schema. It will then validate the JSON output against the schema and print the output to the console.

You will see the output in the console.
   Example:
   ```bash
   {
  "description": null,
  "teams": [
    {
      "name": "Green Bay Packers",
      "score": 0
    },
    {
      "name": "Arizona Cardinals",
      "score": 7
    }
  ],
  "status": "in_progress",
  "quarter": 2,
  "clock_time": "12:12",
  "possession_team": "Green Bay Packers",
  "down": "2nd",
  "distance": 10,
  "yard_line": -10,
  "network": "NBC",
  "is_shown": true
}
```

> [!NOTE]
> You can optionally change the provider and model to test against different models. For example, to test against `llama3.2-vision:11b` using `ollama`, you can run:
> ```bash
> pytest -sv tests/test_instructor.py -k test_instructor_hub_sample --domain media.nfl-game-state --provider ollama --model llama3.2-vision:11b
> ```
