import logging

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{cookiecutter.package_name}} import dependencies
from {{cookiecutter.package_name}}.routers import health

logger = logging.getLogger(__name__)

app = FastAPI(
    dependencies=[Depends(dependencies.get_apikey_header)],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
