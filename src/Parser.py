from abc import ABC, abstractmethod
import requests

'''Абстрактный класс для работы с API сервиса с вакансиями.'''
class Parser(ABC):
    @abstractmethod
    def load_vacancies(self):
        pass

    # @abstractmethod
    # def from_vacancy(self, vacancy):
    #     pass

class HH(Parser):
    '''Класс подключается к API, получает вакансии и записывает их в файл json в читабельном виде'''
    def __init__(self, keyword):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params =  {"text": keyword, "page": 0, "per_page": 100}

    def load_vacancies(self):
        vacancies = []

        while self.params.get('page') != 1:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            vacancies.extend(vacancies)
            self.params['page'] += 1

        return vacancies







