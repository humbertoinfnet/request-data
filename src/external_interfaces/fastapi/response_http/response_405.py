from .interfaces import ResponseHTTP


class ResponseHTTP405(ResponseHTTP):
    """
    Classe responsável por construir a resposta para indicar que o verbo HTTP utilizado não é suportado, por exemplo: a
    requisição ocorre por meio de um GET, porém o único método disponível é o POST.
    """

    def __init__(self, status_code: int = 405, message: str = "Method Not Allowed") -> None:
        super().__init__(status_code=status_code, message=message)
