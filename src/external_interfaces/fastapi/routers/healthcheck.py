from typing import Any
from fastapi import APIRouter

from src.interface_adapters.schemas.response import (
    ResponseError,
    ResponseSuccess
)
from ..response_handler import ResponseHTTPHandler

router = APIRouter(tags=["system"])


@router.get("/healthcheck",
    responses={
        200: {"model": ResponseSuccess},
        500: {"model": ResponseError},
    }
)
def healthcheck() -> Any:
    """
    Rota para monitoramento da integridade do aplicativo.
    """
    return ResponseHTTPHandler.create(status_code=200, data={})
