from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class RequestDataInterface(ABC):
    document: str

    @abstractmethod
    def execute(self):
        raise NotImplementedError('Método não implementado')
