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

        for vacancy in user.get_top_salary():
            print(vacancy)

        for vacancy in user.get_vacancy_from_keyword():
            print(vacancy)

        print("Удачного поиска!")

    user_intaraction()
    #
    # n = int(input("Введите топ: "))
    # user.get_top_salary(n)
    #
    # for vacancy in user.get_vacancies_list(keyword):
    #     vac = Vacancy.new_vacancy(vacancy)
    #     print(vac)
    #     print()
    #     user.vacancies_list.append(vac)
    #
    # for vacancy in user.get_vacancy_from_keyword():
    #     print(vacancy)
    #     print()
