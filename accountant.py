import requests 
from pprint import pprint


url = "https://api.hh.ru/vacancies/"
params = {
    "text": "Бухгалтер",
    "area": "16"
}
response = requests.get(url, params=params)
response.raise_for_status()
vacancies = response.json()
for vacancy in vacancies["items"]:
    salary_from = vacancy["salary"]["from"]
    salary_to = vacancy["salary"]["to"]
    if salary_from and salary_to:
        print("Вакансия: " + vacancy["name"], end=". ")
        print("Город: " + vacancy["area"]["name"], end=". ")
        print(f"Зарплата: от {salary_from} BYR до {salary_to} BYR")
    if salary_from:
        print("Вакансия: " + vacancy["name"], end=". ")
        print("Город: " + vacancy["area"]["name"], end=". ")
        print(f"Зарплата: {salary_from} BYR")

