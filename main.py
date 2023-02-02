from itertools import count

import requests
from pprint import pprint
from terminaltables import AsciiTable


def predict_rub_salary(salary):
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


def get_average_salary(salary_prog):
    try:
        count_vacancies = len(salary_prog)
        average_salary = sum(salary_prog) / count_vacancies
        return int(average_salary), count_vacancies
    except ZeroDivisionError:
        return None, 0 


def table_vacancies(statistics_languages):
    title = "HeadHunter Moscow"
    table_data = [
        ['Язык программирования', 'Вакансий найдено', 'Вакансий обработано', 'Средняя зарплата']]
    for language in statistics_languages:
        stats_languege = []
        stats_languege.append(language)
        stats_languege.append(statistics_languages[language]["vacancies_found"])
        stats_languege.append(statistics_languages[language]["vacancies_processed"])
        stats_languege.append(statistics_languages[language]["average_salary"])
        table_data.append(stats_languege)
    table = AsciiTable(table_data, title)
    print(table.table)


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
table_vacancies(statistics_languages)
    