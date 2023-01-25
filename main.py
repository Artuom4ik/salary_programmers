import requests
from pprint import pprint


def get_average_salary(salary):
    if salary["currency"] == "RUR":
        from_salary = salary["from"]
        to_salary = salary["to"]
        if from_salary and to_salary:
            average_salary = (int(from_salary) + int(to_salary)) * 0.5
            return average_salary
        if from_salary:
            average_salary = int(from_salary) * 1.2
            return average_salary
        if to_salary:
            average_salary = int(to_salary) * 0.8
            return average_salary



id = 73911777
url = f"https://api.hh.ru/vacancies/"
programming_languages = [
        "JavaScript", 
        "Java", 
        "Python",
        "Ruby",
        "PHP",
        "C++",
        "TypeScript",
        "C#",
        "C",
        "Go" 
    ]
found_vacancies = {}
# for programming_language in programming_languages:
#     params = {
#         "area": "1",
#         "text": f"Программист {programming_language}"
#     }
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     vacancies = response.json()
#     # found_vacancies[programming_language] = vacancies["found"]
# print(found_vacancies)
#     for vacancy in vacancies["items"]:
#         print(vacancy["name"])
#         print(vacancy["area"])
params = {
        "area": "1",
        "text": "Программист Python",
        "period": 30
    }
response = requests.get(url, params=params)
response.raise_for_status()
vacancies = response.json()
for vacancy in vacancies["items"]:
    salary = vacancy["salary"]
    print(get_average_salary(salary))
# print(vacancies)