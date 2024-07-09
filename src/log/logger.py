import logging
import json


class Logger:
    """
    Define a instância do logger para registro de eventos.
    """

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        self.logger.addHandler(self.format_logger())
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)

    def get_logger(self) -> logging.Logger:
        """
        Retorna a instância do logger a ser utilizada nos demais processos da aplicação.

        Returns:
            Instância do logger.
        """
        return self.logger
    
    def format_logger(self) -> None:
        """
        Função responsável pela formatação do Logger
        """
        log_format = {
            'asctime': '%(asctime)s',
            'name': '%(name)s',
            'levelname': '%(levelname)s',
            'message': '%(message)r',
            'pathname': '%(pathname)s',
            'lineno': '%(lineno)d',
            'funcName': '%(funcName)s',
            'filename': '%(filename)s'
        }

        formatter = logging.Formatter(json.dumps(log_format, ensure_ascii=False))
        file_handler = logging.FileHandler('src/log/app.log', encoding='utf-8')
        file_handler.setFormatter(formatter)
        return file_handler

class ConfigLogger:

    @classmethod
    def info(self, name_class, name_func, text_add=''):
        if text_add:
            return f"[{name_class}] - passo: execucao do metodo {name_func} | {text_add}"
        return f"[{name_class}] - passo: execucao do metodo {name_func}"

    @classmethod
    def error(self, name_class, name_func, exc=''):
        return f"[{name_class}] - passo: execucao do metodo {name_func} - problema: {exc}"
