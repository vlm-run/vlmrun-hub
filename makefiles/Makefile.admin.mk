VLMRUN_HUB_VERSION := $(shell python -c 'from vlmrun.hub.version import __version__; print(__version__.replace("-", "."))')
PYPI_USERNAME :=
PYPI_PASSWORD :=

WHL_GREP_PATTERN := .*\$(VLMRUN_HUB_VERSION).*\.whl

create-pypi-release-test:
	@echo "looking for vlmrun-hub whl file..."
	@for file in dist/*; do \
		echo "examining file: $$file"; \
		if [ -f "$$file" ] && echo "$$file" | grep -qE "$(WHL_GREP_PATTERN)"; then \
			echo "Uploading: $$file"; \
			twine upload --repository testpypi "$$file"; \
		fi; \
	done
	@echo "Upload completed"


create-pypi-release:
	@echo "looking for vlmrun-hub whl file..."
	@for file in dist/*; do \
		echo "examining file: $$file"; \
		if [ -f "$$file" ] && echo "$$file" | grep -qE "$(WHL_GREP_PATTERN)"; then \
			echo "Uploading: $$file"; \
			twine upload "$$file"; \
		fi; \
	done
	@echo "Upload completed"

create-tag:
	git tag -a ${VLMRUN_HUB_VERSION} -m "Release ${VLMRUN_HUB_VERSION}"
	git push origin ${VLMRUN_HUB_VERSION}
