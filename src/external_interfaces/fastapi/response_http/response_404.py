from .interfaces import ResponseHTTP


class ResponseHTTP404(ResponseHTTP):
    """
    Classe responsável por construir a resposta para indicar que o servidor não conseguiu encontrar o recurso
    solicitado.
    """

    def __init__(self, status_code: int = 404, message: str = "Not Found") -> None:
        super().__init__(status_code=status_code, message=message)
