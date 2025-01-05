__all__ = ["import_all"]


def import_all():
    from vlmrun.hub.constants import VLMRUN_HUB_CATALOG_PATH
    from vlmrun.hub.registry import Registry, SchemaCatalogYaml

    # Load the catalog
    catalog = SchemaCatalogYaml.from_yaml(VLMRUN_HUB_CATALOG_PATH)

    # Register all schemas from the catalog.yaml
    for schema in catalog.schemas:
        Registry.register(schema.domain, schema.schema_class)
