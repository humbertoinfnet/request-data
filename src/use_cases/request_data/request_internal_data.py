from dataclasses import dataclass
from faker import Faker
import random
from .interface import RequestDataInterface


@dataclass
class RequestInternalData(RequestDataInterface):
    document: str

    def __pos_init__(self):
        self.data: dict
        self.fake = Faker()

    def execute(self):
        self.get_data()
        return self.data

    def get_data(self):
        self.data = {
            'informacoes_cadastrais': self.simulate_data_cadastral_info(),
            'informacoes_transacionais': self.simulate_data_cadastral_info()
        }

    def simulate_data_cadastral_info(self):
        return {
            'abertura_conta': self.fake.date_this_decade(),
            'categoria_conta': random.choice(['pequena', 'normal', 'grande']),
            'classficacao_conta': random.choice(['A', 'B', 'C','D','E','Fraude']),
        }

    def simulate_data_transaction(self):
        return {
            'media_transacoes_tres_meses': self.fake.pydecimal(max_value=5000, right_digits=2, positive=True),
            'quantidade_transacoes': self.fake.random_int(min=1, max=100),
            'saldo': self.fake.pydecimal(left_digits=5, right_digits=2, positive=True),
            'faturamento': self.fake.pydecimal(max_value=1_000_000, min_value=50_000, right_digits=0, positive=True),
        }
