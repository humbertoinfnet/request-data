from pydantic import Field, BaseModel
from .response_default import ResponseDefault


class ResponseNotFound(ResponseDefault):
    message: str = Field("Resource not found!", description="Exception Information")
