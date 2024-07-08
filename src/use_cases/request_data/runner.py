from dataclasses import dataclass
from .request_internal_data import RequestInternalData
from .request_data_cnpj import RequestInfoCnpj
from .request_credit_bureau import RequestCreditBureau
from src.interface_adapters.request_info_cnpj.request_info_cnpj_interface import RequestInfoCnpjInterface
from src.log import logger, log
import inspect


@dataclass
class Runner:
    document: str
    request_info_cnpj: RequestInfoCnpjInterface

    __name__ = 'Runner'

    def execute(self):
        logger.info(log.info(self.__name__, inspect.currentframe().f_code.co_name))
        data = {}
        data.update(RequestInternalData(self.document).execute())
        data.update(RequestCreditBureau(self.document).execute())
        data.update(RequestInfoCnpj(self.document, self.request_info_cnpj).execute())
        return data
