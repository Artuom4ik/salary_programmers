from terminaltables import AsciiTable

from get_vacancy import get_headhunter_vacancies


def table_vacancies(statistics_languages):
    title = "HeadHunter Moscow"
    table_data = [
        [
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата']]
    for language, params in statistics_languages.items():
        stats_languege = [
            language,
            params["vacancies_found"],
            params["vacancies_processed"],
            params["average_salary"]
        ]
        table_data.append(stats_languege)
    table = AsciiTable(table_data, title)
    print(table.table)


if __name__ == "__main__":
    statistics_languages = get_headhunter_vacancies()
    table_vacancies(statistics_languages)
