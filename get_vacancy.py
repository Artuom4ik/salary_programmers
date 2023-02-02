from itertools import count

import requests

from get_average_salary import predict_rub_salary, get_average_salary


def get_headhunter_vacancies():
    url = "https://api.hh.ru/vacancies/"
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
    statistics_languages = {}
    for programming_language in programming_languages:
        vacancies_prog = {}
        salaries_prog = []
        for page in count(0):
            params = {
                "area": "1",
                "text": f"Программист {programming_language}",
                "per_page": 100,
                "page": page,
                "period": 30
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            vacancies = response.json()
            if page >= 19:
                break
            for vacancy in vacancies["items"]:
                salary = vacancy["salary"]
                if not salary:
                    continue
                if salary["currency"] != "RUR":
                    continue
                vacancy_salary = predict_rub_salary(salary)
                if not vacancy_salary:
                    continue
                salaries_prog.append(vacancy_salary)
        average_salary, vacancies_processed = get_average_salary(salaries_prog)
        vacancies_prog["vacancies_processed"] = vacancies_processed
        vacancies_prog["average_salary"] = average_salary
        vacancies_prog["vacancies_found"] = vacancies["found"]
        statistics_languages[programming_language] = vacancies_prog
    return statistics_languages
