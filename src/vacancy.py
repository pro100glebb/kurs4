import json

class Vacancy():
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, area: str, salary: int, url: str, snippet: str):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.salary = salary
        self.url = url
        self.snippet = snippet

    def __str__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else "Не указана"}\n"
                f"Ссылка: {self.url}\n"
                f"Сниппет: {self.snippet}\n")

    def __lt__(self, other):
        if not self.salary:
            return "Зарплата не указана в первой вакансии"
        elif not other.salary:
            return "Зарплата не указана во второй вакансии"
        elif self.salary < other.salary:
            return True
        else:
            return False


    @staticmethod
    def __validation_data(data):
        if data:
            return data
        else:
            return "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy):
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        if vacancy.get("salary"):
            salary = vacancy.get("salary").get("from")
        else:
            salary = 0
        url = vacancy.get("url")
        snippet = vacancy.get("snippet").get("requirement")
        return cls(name, area, salary, url, snippet)









