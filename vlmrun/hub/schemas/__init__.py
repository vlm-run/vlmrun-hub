from typing import Optional, Tuple

from loguru import logger

from vlmrun.hub.constants import VLMRUN_HUB_CATALOG_PATH, VLMRUN_HUB_PATH

__all__ = ["import_all"]


def import_all(catalog_paths: Optional[Tuple[str]] = (VLMRUN_HUB_PATH / "schemas/contrib/catalog.yaml",)):
    from vlmrun.hub.registry import Registry, SchemaCatalogYaml

    # Load the catalog
    catalog = SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CATALOG_PATH)

    # Register all schemas from the catalog.yaml
    for schema in catalog.schemas:
        Registry.register(schema.domain, schema.schema_class)

    # Register additional schemas from the provided paths
    if catalog_paths is not None:
        for path in catalog_paths:
            catalog = SchemaCatalogYaml.from_yaml(path)
            for schema in catalog.schemas:
                Registry.register(schema.domain, schema.schema_class)

    logger.debug(f"\n{Registry.get()}")
