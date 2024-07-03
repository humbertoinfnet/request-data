from abc import ABC, abstractmethod


class RequestInfoCnpjInterface(ABC):

    @abstractmethod
    def execute(self, document: str):
        raise NotImplementedError('Método não implementado')

    @abstractmethod
    def _request_data(self, document: str):
        raise NotImplementedError('Método não implementado')
    
    @abstractmethod
    def _adapter(self, data: dict):
        raise NotImplementedError('Método não implementado')
