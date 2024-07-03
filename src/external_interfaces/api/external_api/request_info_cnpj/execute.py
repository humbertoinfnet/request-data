from dataclasses import dataclass
import requests
from src.interface_adapters.request_info_cnpj.request_info_cnpj_interface import RequestInfoCnpjInterface


@dataclass
class RequestInfoCnpj(RequestInfoCnpjInterface):

    def execute(self, document: str):
        data = self._request_data(document)
        data_adapter = self._adapter(data)
        return data_adapter

    def _request_data(self, document: str):
        url = f'https://api.cnpjs.dev/v1/{document}'
        resp = requests.get(url)
        return resp.json()
    
    def _adapter(self, data):
        return data
