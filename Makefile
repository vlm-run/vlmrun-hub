lint: ## Format source code automatically
	pre-commit run --all-files

test: ## Run tests
	pytest tests/hub/schemas
