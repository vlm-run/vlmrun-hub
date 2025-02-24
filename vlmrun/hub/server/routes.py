import hashlib
import json
from typing import List, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from vlmrun.hub.registry import registry
from vlmrun.hub.version import __version__

router = APIRouter()


class HubInfoResponse(BaseModel):
    version: str = Field(..., description="The version of the hub")


class HubDomainInfo(BaseModel):
    domain: str = Field(..., description="The domain identifier")
    description: Optional[str] = Field(None, description="Description of the schema's purpose")
    supported_inputs: Optional[List[str]] = Field(None, description="List of supported input types")
    tags: Optional[List[str]] = Field(None, description="List of tags for the schema")
    sample_data: Optional[List[str]] = Field(None, description="URLs to sample data")


class HubSchemaRequest(BaseModel):
    domain: str = Field(..., description="The domain to get the schema for")


class HubSchemaResponse(BaseModel):
    json_schema: dict = Field(..., description="The JSON schema for the domain")
    schema_version: str = Field(..., description="The specific version of the schema")
    schema_hash: str = Field(..., description="The first 8 characters of the sha256 hash")


@router.get("/info", response_model=HubInfoResponse)
def info() -> HubInfoResponse:
    """Get hub version information."""
    return HubInfoResponse(version=__version__)


@router.get("/domains", response_model=List[HubDomainInfo])
def list_domains() -> List[HubDomainInfo]:
    """List available domains."""
    return [HubDomainInfo(domain=domain, **registry.get_domain_info(domain)) for domain in registry.list_schemas()]


@router.get("/domains/{domain}", response_model=bool)
def has_domain(domain: str) -> bool:
    """Check if domain exists."""
    return domain in registry


@router.post("/schema", response_model=HubSchemaResponse)
async def get_domain_schema(request: HubSchemaRequest) -> HubSchemaResponse:
    """Get schema for domain."""
    try:
        schema_class = registry[request.domain]
        json_schema = schema_class.model_json_schema()
        schema_hash = hashlib.sha256(json.dumps(json_schema, sort_keys=True).encode()).hexdigest()[:8]

        return HubSchemaResponse(
            json_schema=json_schema,
            schema_version=__version__,
            schema_hash=schema_hash,
        )
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Schema '{request.domain}' not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
