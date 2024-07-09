from dataclasses import dataclass
from faker import Faker
import random
from src.log import logger, log
import inspect


@dataclass
class RequestCreditBureau:
    document: str

    __name__ = 'RequestCreditBureau'

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
            'informacoes_bureau_credito': self.simulate_credit_info()
        }

    def simulate_credit_info(self):
        population = [0, 1, 2, 3, 4, 5, 6]
        weights = [0.7, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
        anotacoes_negativas = random.choices(population, weights=weights)[0]
        return {
            'score_risco': self.fake.random_int(min=100, max=1000),
            'pendencia_financeira': self.fake.pydecimal(max_value=5000, right_digits=0, positive=True) if anotacoes_negativas else 0,
            'anotacoes_negativas': anotacoes_negativas
        }
