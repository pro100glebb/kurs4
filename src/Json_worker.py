import json
import os
from abc import ABC, abstractmethod



class FileWork(ABC):
    """Класс для работы с файлом"""

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def save_file(self, data):
        pass

    @abstractmethod
    def delite_file(self):
        pass

class WorkWithJson(FileWork):
    def __init__(self, abs_pash="data/vacancies.json"):
        self._abs_path = os.path.abspath(abs_pash)

    def read_file(self):
        """Метод для чтения файла"""
        with open(self._abs_path, "r") as file:
            return json.load(file)

    def save_file(self, data):
        """Метод для сохранение файла"""
        with open(self._abs_path, "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delite_file(self):
        with open(self._abs_path, "w") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
