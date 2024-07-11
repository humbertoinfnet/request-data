from dataclasses import dataclass
from faker import Faker
import random
import arrow
from src.log import logger, log
import inspect


@dataclass
class RequestInternalData:
    document: str

    __name__ = 'RequestInternalData'

    def __post_init__(self):
        self.data: dict
        self.fake = Faker()

    def execute(self):
        try:
            logger.info(log.info(self.__name__, inspect.currentframe().f_code.co_name))
            self.get_data()
            return self.data
        except Exception as err:
            logger.error(log.error(self.__name__, inspect.currentframe().f_code.co_name, err))
        return {}

    def get_data(self):
        self.data = {
            'informacoes_cadastrais': self.simulate_data_cadastral_info(),
            'informacoes_transacionais': self.simulate_data_transaction()
        }

    def simulate_data_cadastral_info(self):
        account_opening = self.fake.date_this_decade(before_today=True)
        account_age = (arrow.now() - arrow.get(account_opening)).days
        return {
            'abertura_conta': account_opening,
            'tempo_conta': account_age,
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
