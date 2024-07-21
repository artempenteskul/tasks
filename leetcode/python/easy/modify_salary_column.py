# task number - 2884


import pandas as pd


def modify_salary_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'].apply(lambda x: x * 2)
    return employees
