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