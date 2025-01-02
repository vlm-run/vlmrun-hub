from pydantic import BaseModel


class Registry:
    """Registry for schemas."""

    _instance: "Registry" = None
    """Singleton instance of the registry."""

    schemas: dict[str, BaseModel] = {}
    """Dictionary of registered schemas."""

    @classmethod
    def get(cls) -> "Registry":
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def register(cls, name: str, schema: BaseModel):
        cls.get().schemas[name] = schema

    def __contains__(self, name: str) -> bool:
        return name in self.schemas

    def __getitem__(self, name: str) -> BaseModel:
        return self.schemas[name]

    @classmethod
    def list(cls) -> list[str]:
        return list(cls.schemas.keys())
