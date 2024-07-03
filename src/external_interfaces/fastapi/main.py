# pylint: disable=unused-argument
from typing import Any, Callable
import uuid
import importlib
import json
import pkgutil
import time

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .response_handler import ResponseHTTPHandler
from src.log import logger


version_data = {}
try:
    with open("version.json", "r", encoding="utf-8") as ver_file:
        version_data = json.load(ver_file)
except Exception as error:
    logger.error(f"Leitura versão falhou: {error} - utilizando valor default: 1.0.0")

app = FastAPI(
    title="Python Base",
    description="Estrutura default para projetos Python",
    version=version_data.get("version", "1.0.0"),
    contact={
        "name": "",
        "email": "",
    },
    redoc_url="/documentation",
    docs_url="/swager",
)

# Log a message using the logger
logger.info("Starting FastAPI application")

@app.middleware("http")
async def add_request_extras_to_context(request: Request, call_next: Callable) -> Any:
    """
    Método responsável por definir um uuid distinto ao contexto de cada requisição.
    """

    if "healthcheck" in getattr(request, "scope", {}).get("path", ""):
        response = await call_next(request)
        return response

    extra_logs = {
        "uuid": str(uuid.uuid4()),
        "hostname": getattr(request, "headers", {}).get("host", ""),
        "version": getattr(getattr(request, "app", ""), "version", ""),
        "req": {
            "path": getattr(request, "scope", {}).get("path", ""),
            "agent": getattr(request, "headers", {}).get("user-agent", ""),
            "method": getattr(request, "method", ""),
            "ip": getattr(getattr(request, "client", ""), "host", ""),
        },
        "query_params": dict(getattr(request, "query_params", {})),
        "path_params": dict(getattr(request, "path_params", {})),
    }

    logger.info("Requisição http iniciada")

    del extra_logs["req"]
    del extra_logs["query_params"]
    del extra_logs["path_params"]

    req_start_time = time.time()
    response = await call_next(request)
    req_end_time = round(time.time() - req_start_time, 3)

    extra_logs["res"] = {}
    extra_logs["res"]["time"] = req_end_time
    extra_logs["res"]["status"] = getattr(response, "status_code", "")

    logger.info("Requisição http finalizada")

    return response


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> Any:
    """
    Define um handler para tratar exceções de HTTP e formatar a resposta par aos padrões da aplicação.

    Args:
        request: requisição recebida pelo fastapi
        exc: Exceção lançada pelo fastapi

    Returns:
        JSONResponse com o status do erro encontrado e o conteúdo é um dicionário com as chaves:
        status_code, message e data
    """
    return ResponseHTTPHandler.create(status_code=exc.status_code, data={})


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError) -> Any:
    """
    Define um handler para tratar exceções de HTTP de validação da requisição.

    Args:
        request: requisição recebida pelo fastapi
        exc: Exceção lançada pelo fastapi

    Returns:
        JSONResponse com o status do erro encontrado e o conteúdo é um dicionário com as chaves:
        status_code, message e data
    """
    return ResponseHTTPHandler.create(status_code=400, data={"errors": exc.errors()})


def import_routers(directory: str) -> None:
    """Método que importa as rotas do projeto de forma dinâmica.

    Args:
        directory: caminho do módulo onde as rotas a serem importadas estão.
    """
    for _, module_name, _ in pkgutil.iter_modules([directory]):
        try:
            module = importlib.import_module(f"{directory.replace('/', '.')}.{module_name}")
            if hasattr(module, "__path__"):
                import_routers(f"{directory}/{module_name}")
            else:
                app.include_router(module.router)
        except Exception as exc:
            logger.error(f"[import_routers] - passo: executando import_routers - problema: {exc} | module_name: {module_name}")


import_routers("src/external_interfaces/fastapi/routers")
