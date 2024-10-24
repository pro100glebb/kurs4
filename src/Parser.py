from abc import ABC, abstractmethod
import requests

'''Абстрактный класс для работы с API сервиса с вакансиями.'''
class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass


class HH(Parser):
    '''Класс подключается к API, получает вакансии и записывает их в файл json в читабельном виде'''
    def __init__(self, keyword):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self.params =  {"text": keyword, "page": 0, "per_page": 100}

    def load_vacancies(self):
        """Медтод получает список вакансий с hh.ru"""
        vacancies = []
        while self.params.get('page') != 1:
            raw_vacancies = self._get_api()
            vacancies.extend(raw_vacancies)
            self.params['page'] += 1

        return vacancies

    def _get_api(self):
        response = requests.get(self._url, headers=self._headers, params=self.params)
        return response.json()["items"]









