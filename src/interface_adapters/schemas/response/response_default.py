from pydantic import BaseModel, Field


class ResponseDefault(BaseModel):
    status_code: int = Field("status de resposta", description="Status do response")
    message: str = Field("mensagem de sucesso", description="Mensagem do response")
    data: dict = Field(description="Dados do retorno da rota")
