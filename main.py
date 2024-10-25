from src.Parser import HH
from src.Json_worker import WorkWithJson
from src.user_inteactive import UserInteractive
from src.vacancy import Vacancy

if __name__ == "__main__":

    def user_intaraction():
        """Функция для взаимодействия с пользователем"""
        print("Привет!\n")
        user_name = input("Введите имя: ")
        user = UserInteractive(user_name)
        keyword = input("Введите название вакансии: ")

        for vacancy in user.get_vacancies_list(keyword):
            vac = Vacancy.new_vacancy(vacancy)
            user.vacancies_list.append(vac)
            print(vac)

        user.save_to_file()

        n = int(input("Введите количество вакансий для вывода в топ N: "))
        for vacancy in user.get_top_salary(n):
            print(vacancy)

        for vacancy in user.get_vacancy_from_keyword():
            print(vacancy)

        print("Удачного поиска!")

    user_intaraction()

