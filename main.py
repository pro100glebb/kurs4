from src.Parser import HH
from src.Json_worker import WorkWithJson
from src.user_inteactive import UserInteractive
from src.vacancy import Vacancy

if __name__ == "__main__":

    print("Hello user")
    user_name = input("Введите имя: ")
    user = UserInteractive(user_name)

    keyword = input("Введите запрос: ")

    for vacancy in user.get_vacancies_list(keyword):
        vac = Vacancy.new_vacancy(vacancy)
        print(vac)
        print()
        user.vacancies_list.append(vac)

    for vacancy in user.get_vacancy_from_keyword():
        print(vacancy)
        print()


