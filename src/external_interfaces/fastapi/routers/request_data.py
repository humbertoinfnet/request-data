from typing import Any
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder

from src.interface_adapters.schemas.response import (
    ResponseError,
    ResponseSuccess
)
from src.log import logger
from ..response_handler import ResponseHTTPHandler
from src.use_cases.request_data.request_data_cnpj import HandleRequestInfoCnpj
from src.external_interfaces.api.external_api.request_info_cnpj import RequestInfoCnpj
router = APIRouter(tags=["examples"])


@router.get(
    "/customer-information",
    responses={
        200: {"model": ResponseSuccess},
        500: {"model": ResponseError},
    },
)
def request_data(
    document: str = Query(
        default=...,
        description="Documento do cliente (somente números)",
    ),
) -> Any:
    """
    Rota de exemplo para busca de dados gerais de clientes.
    """
    logger.info("[customer_information] - passo: executando a rota GET /customer-information")
    try:
        handle_request_external_info_cnpj = HandleRequestInfoCnpj(document=document, request_data=RequestInfoCnpj())
        data = handle_request_external_info_cnpj.execute()
        return ResponseHTTPHandler.create(status_code=200, data=jsonable_encoder(data))
    except Exception as exc:
        logger.info(f"[customer_information] - passo: executando a rota GET /customer-information - problema: {exc}")
        return ResponseHTTPHandler.create(status_code=500, data={})
