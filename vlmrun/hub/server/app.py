from fastapi import FastAPI

from vlmrun.hub.server.routes import router
from vlmrun.hub.version import __version__

app = FastAPI(
    title="VLM Run Hub",
    description="API server for VLM Run Hub schema registry",
    version=__version__,
    docs_url="/docs",
)

app.include_router(router, prefix="")
