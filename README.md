# VLM Run Hub

VLM Run Hub for various industry-specific schemas

## Overview

This repository contains a collection of standardized schemas for various industries, designed to work with Vision Language Models (VLMs). The schemas are organized by industry sectors and use cases.

## Schema Organization

The schemas are organized in the following structure:

## Schema Design Principles

1. **Pydantic Base Models**: All schemas are implemented using Pydantic BaseModel for robust type validation and serialization.
2. **Optional Fields**: Most fields are optional (using `| None`) to accommodate varying data availability.
3. **Field Descriptions**: Every field includes a descriptive comment explaining its purpose.
4. **Nested Structures**: Complex data types are broken down into nested models for better organization.

## Industry Sectors

### Banking

- Document verification schemas for KYC and compliance

### Document Processing

- ID extraction for identity documents
- Invoice parsing and structuring
- Presentation content extraction

### Healthcare

- Medical insurance card information
- Patient intake form processing

### Media

- NBA game state tracking
- NFL game state tracking

### Retail

- E-commerce product captioning and categorization

### Aerospace

- Remote sensing image classification

## Schema Validation

All schemas include:

- Type validation
- Optional/required field specifications
- Nested model support
- Enumerated types where applicable
- Comprehensive field descriptions

## Contributing

### Using LLMs to Generate New Schemas

When creating new industry-specific schemas, you can leverage Large Language Models (LLMs) to help generate well-structured Pydantic models. Here's the recommended approach:

1. **Define the Domain**

   - Identify the specific industry or use case
   - List key data points that need to be captured
   - Reference existing industry standards or documentation

2. **Prompt Engineering**
   Example prompt template: ```
   Create a Pydantic schema for [industry/use-case] that:

   - Captures [key data points]
   - Uses proper type hints
   - Includes field descriptions
   - Follows existing patterns from similar schemas
   - Implements nested models where appropriate ```

3. **Schema Structure Guidelines**
   Follow these patterns from existing schemas:

   - Use nested models for complex data (see `retail/ecommerce_product_caption.py`)
   - Implement enums for fixed choices (see `aerospace/remote_sensing.py`)
   - Make fields optional with `| None` (see `document/invoice.py`)
   - Add comprehensive descriptions using `Field()` (see all schemas)
   - Use appropriate data types (str, int, float, date, etc.)

4. **Validation and Testing**

   - Ensure the generated schema validates correctly
   - Test with sample data
   - Review field descriptions for clarity
   - Check type hints and optional fields

5. **Documentation**
   - Add the schema to the appropriate section in this README
   - Include example usage if helpful
   - Document any special types or enums

### Example Schema Generation

Looking at existing schemas for inspiration:

- For document processing, reference `document/id_extraction.py` for handling multiple related data points
- For classification tasks, reference `aerospace/remote_sensing.py` for enum usage
- For complex nested structures, reference `retail/ecommerce_product_caption.py`
- For financial data, reference `banking/document_verification.py`

### Best Practices

1. Keep models focused and specific to the use case
2. Use clear, descriptive field names
3. Include comprehensive field descriptions
4. Make fields optional unless absolutely required
5. Use appropriate data types and validation
6. Follow existing patterns for similar data structures
