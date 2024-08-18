
class Vacancy():
'''Класс для работы с вакансиями'''
    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = self.validate(salary)
        self.description = description

    @staticmethod
    def validate(self, salary):
        return salary or 0


