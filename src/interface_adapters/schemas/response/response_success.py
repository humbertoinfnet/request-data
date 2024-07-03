from pydantic import Field
from .response_default import ResponseDefault


class ResponseSuccess(ResponseDefault):
    ResponseDefault.data = Field(description="Dados do retorno da rota")
