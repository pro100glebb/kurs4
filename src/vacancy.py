import json

class Vacancy():
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, area: str, url: str, snippet: str, salary: int):
        self.name = self.__validation_data(name)
        self.area = self.__validation_data(area)
        self.url = self.__validation_data(url)
        self.snippet = self.__validation_data(snippet)
        self.salary = salary

    def __repr__(self):
        return (f"{self.name}\n"
                f"Город: {self.area}\n"
                f"Зарплата: {self.salary if self.salary else "Не указана"}\n"
                f"Ссылка: {self.url}\n"
                f"Сниппет: {self.snippet}\n")

    def __lt__(self, other):
        """Метод сравнения вакансий по ЗП"""
        try:
            if self.salary < other.salary:
                return True
            else:
                return False
        except AttributeError:
            print("Зарплата не указана")
            raise

    @staticmethod
    def __validation_data(data):
        if data:
             return data
        else:
             return "Отсутствует"

    @classmethod
    def new_vacancy(cls, vacancy):
        """Метод достает нужную нам информацию о вакансии из json"""
        name = vacancy.get("name")
        area = vacancy.get("area").get("name")
        url = vacancy.get("url")
        snippet = vacancy.get("snippet").get("requirement")
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary = vacancy.get("salary").get("from")
            else:
                salary = 0
        else:
            salary = 0
        return cls(name, area, url, snippet, salary)









