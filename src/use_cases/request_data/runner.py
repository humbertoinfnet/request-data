from .interface import RequestDataInterface


class Runner:

    def execute(self, document: str):
        data = {}
        for execute in RequestDataInterface.__subclasses__():
            data.update(execute(document).execute())