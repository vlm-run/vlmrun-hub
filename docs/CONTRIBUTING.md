# Contributing to VLM Run Hub

We welcome contributions to the VLM Run Hub! Whether you're reporting bugs, suggesting features, or contributing code, your input is valuable to us.

## Reporting Bugs and Asking Questions

- **GitHub Issues**: Use the [GitHub Issues](https://github.com/vlm-run-hub/issues) to report bugs or request features.
- **Discussions**: Join our [Discord forum](https://discord.gg/4jgyECY4rq) for general questions and discussions.

## Contributing Code

1. **Fork the Repository**: Start by forking the repository and cloning it to your local machine.

2. **Set Up Your Development Environment**: Follow the instructions in the `README.md` to set up your development environment.

3. **Create a Branch**: Create a new branch for your feature or bug fix.

4. **Write Tests**: Ensure your code is well-tested. We use `pytest` for testing. Use `make test` to run all the tests.

5. **Submit a Pull Request**: Once your changes are ready, submit a pull request. Make sure to follow the [Schema Guidelines](./SCHEMA-GUIDELINES.md) if your contribution involves Pydantic schema changes.

## Schema Contributions

For contributions involving Pydantic schemas, please refer to the [Schema Guidelines](./SCHEMA-GUIDELINES.md) for detailed instructions on creating and submitting schemas.

## Review Process

- **For Members**: Assign a reviewer to your pull request. Address any feedback and ensure all tests pass before merging.
- **For Non-Members**: A project member will be assigned to review your pull request. Please address their feedback promptly.

## PR Checklist

Before submitting your changes, ensure:

- Make any relevant changes to the repository.
- Run `make lint` to ensure your code is linted.
- Add any relevant tests under `tests/`, and run `make test` to ensure all tests pass.
- If you are contributing a new schema, follow the [Contributing Schemas](./CONTRIBUTING-SCHEMA.md) instead of the general contributing guidelines.

Thank you for helping us maintain high standards for schema contributions!
