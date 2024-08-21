
class Vacancy():
    """Класс для работы с вакансиями"""
    def __init__(self, name: str, url: str, salary: int | None, description: str | None):
        self.name = name
        self.url = url
        self.salary = self.validate(self, salary)
        self.description = description

    @staticmethod
    def validate(self, salary: int | None) -> int:
        return salary or 0

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        pass
    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)




