import pytest
from src.vacancy import Vacancy
import json

def test_lt():
    vacancy_1 = Vacancy(f"testname", f"testarea", f"testurl", f"testsnippet", salary=500)
    vacancy_2 = Vacancy(f"testname", f"testarea", f"testurl", f"testsnippet", salary=1000)

    assert vacancy_1.__lt__(vacancy_2)
    assert vacancy_2.__lt__(vacancy_1) == False

def test_validation_data():

    x = '{"name":"vacancy_name", "area":{"name":"area_name"}, "url":"vacancy_url", "snippet": {"requirement":"vacency_snippet"}, "salary":{"from":1000}}'
    # parse x:
    y = json.loads(x)

    vacancy_4 = Vacancy.new_vacancy(y)

    assert vacancy_4.name == "vacancy_name"
    assert vacancy_4.area == "area_name"
    assert vacancy_4.url == "vacancy_url"
    assert vacancy_4.snippet == "vacency_snippet"
    assert vacancy_4.salary == 1000


