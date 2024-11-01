import pytest
from src.user_inteactive import UserInteractive
from src.vacancy import Vacancy


@pytest.fixture
def test():
    test = UserInteractive("name")
    test_list = [Vacancy(f"testname {i}", f"testarea {i}", f"testurl {i}", f"testsnippet {i}", salary=i*1000) for i in
                 range(10)]
    test.vacancies_list = test_list
    return test


def test_get_top_salary(test):
    assert test.get_top_salary(0) == []

def test_get_top_salary_3(test):
    assert test.get_top_salary(1)[0].salary == 9000

def test_get_vacancy_from_keyword(test):
    assert test.get_vacancy_from_keyword("ABC") == []

def test_get_vacancy_from_keyword_1(test):
    assert len(test.get_vacancy_from_keyword("testname")) == 10
