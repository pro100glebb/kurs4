import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class AbstractWorker(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Vacancy):
        pass

class JsonFileWorker(AbstractWorker):
    def __init__(self, file_name: str = 'vacancy_json'):
        self._file_name = file_name

    def read(self):
            with open(self._file_name, 'r') as file:
                data = json.load(file)
            return data

    def add_vacancy(self, vacancy: Vacancy):
        data = self.read()
        data.append(vacancy.__dict__)
        with open(self._file_name, 'w') as file:
            json.dump(data, file)

    def remove_vacancy(self, vacancy: Vacancy):
        data = self.read()
        data.remove(vacancy.__dict__)
        with open(self._file_name, 'w') as file:
            json.dump(data, file)

j1 = JsonFileWorker("test.json")
print(j1.remove_vacancy(Vacancy('Swar', 'owgnfwonf', 60000, 'efwf')))
