import json
from abc import ABC, abstractmethod
from typing import Any

import requests

'''Абстрактный класс для работы с API сервиса с вакансиями.'''
class AbstractApi(ABC):
    @abstractmethod
    def get_request(self, *args):
        pass

    @abstractmethod
    def from_vacancy(self, vacancy):
        pass

class HH(AbstractApi):
    '''Класс подключается к API, получает вакансии и записывает их в файл json в читабельном виде'''
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def get_request(self, keyword, page):
        params = {
            "text": keyword,
            "page": page
        }
        return requests.get(self.url, params=params, headers=self.headers)

    def from_vacancy(self, vacancies: list[dict[str, Any]]):
        vacancies_ok = []
        for vacancy in vacancies:
            vacancies_ok.append(vacancy(name=vacancy["name"]))
        pass





