from src.Parser import HH
from src.Json_worker import WorkWithJson

if __name__ == "__main__":
# Создание экземпляра класса для работы с API сайтов с вакансиями
    hh = HH("слесарь")

    vacancies_list = hh.load_vacancies()
    json_worker = WorkWithJson()
    json_worker.save_file(vacancies_list[0])




# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies()
# '''"["items":{"name":"Python tratata", "salary":50}]"'''
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
# '''[{"name":"tratata", "salary":50}, {}, {}]'''
# '''vacancies_list = [Vacancy]'''
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JsonFileWorker()
# json_saver.save() '''создашь файл пустой и сохранишь в него весь список полученных вакансий из vacancies_list'''
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)



