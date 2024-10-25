from typing import Any

from src.Parser import HH
from src.vacancy import Vacancy
from src.Json_worker import WorkWithJson


class UserInteractive():
    """Класс для взаимодействия с пользователем"""

    def __init__(self, user_name):
        self.user_name = user_name
        self.vacancies_list = []

    @staticmethod
    def get_vacancies_list(keyword):
        hh = HH(keyword)
        return hh.load_vacancies()

    def get_top_salary(self, n):
        """Метод сортирует вакансии по ЗП"""
        # n = int(input("Введите количество вакансий для вывода в топ N: "))

        sort_by_salary = list(sorted(self.vacancies_list, key=lambda x: x.salary, reverse=True))
        return sort_by_salary[:n]

    def get_vacancy_from_keyword(self):
        """Метод для фильтрации вакансий по ключеваому слову"""
        keywords = input("Введите ключевые слова: ")
        res = []
        for vacancy in self.vacancies_list:
            if vacancy.name.find(keywords) != -1:
                res.append(vacancy)
        return res

    def save_to_file(self):
        js = WorkWithJson()
        vacancies_dict = [v.__dict__ for v in self.vacancies_list]
        js.save_file(vacancies_dict)

