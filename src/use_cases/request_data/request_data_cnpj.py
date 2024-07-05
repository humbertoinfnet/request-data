from dataclasses import dataclass
import itertools
import arrow
from src.interface_adapters.request_info_cnpj.request_info_cnpj_interface import RequestInfoCnpjInterface
from .interface import RequestDataInterface


@dataclass
class HandleRequestInfoCnpj(RequestDataInterface):
    document: str
    request_data: RequestInfoCnpjInterface

    def __pos_init__(self):
        self.data: dict

    def execute(self):
        self.get_data()
        self.transform_data()
        return {'informacoes_receita_federal': self.data}

    def get_data(self):
        self.data = self.request_data.execute(self.document)

    def transform_data(self):
        itertools.chain(
            self.number_of_partners(self.data),
            self.age_company(self.data),
            self.email_provider(self.data),
        )

    @classmethod
    def number_of_partners(cls, data):
        data['qtde_socios'] = len(data.get('socios', []))
        return data
    
    @classmethod
    def age_company(cls, data):
        if data.get('data_inicio_atividade') is not None:
            data['idade_cnpj_dias'] = (arrow.now() - arrow.get(data.get('data_inicio_atividade'))).days
        else:
            data['idade_cnpj_dias'] = 0
        return data
    
    @classmethod
    def email_provider(cls, data):
        if data.get('email') is not None:
            data['provedor_email'] = data.get('email').split('@')[-1]
        else:
            data['provedor_email'] = 'sem_email'
        return data