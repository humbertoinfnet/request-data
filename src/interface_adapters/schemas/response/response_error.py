from pydantic import Field, BaseModel
from .response_default import ResponseDefault


class DataError(BaseModel):
    error: str = Field("detalhe do erro", description="Mensagem do response")


class ResponseError(ResponseDefault):
    message: str = Field("mensagem de erro", description="Mensagem do response")
    data: DataError
