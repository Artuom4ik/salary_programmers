from terminaltables import AsciiTable

from get_vacancy import get_headhunter_vacancies


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


if __name__ == "__main__":
    statistics_languages = get_headhunter_vacancies()
    table_vacancies(statistics_languages)
    