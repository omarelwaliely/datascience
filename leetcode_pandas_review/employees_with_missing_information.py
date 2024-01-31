import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    res = employees.merge(salaries, on = 'employee_id', how = 'outer')
    return res[(res['salary'].isna()) | (res['name'].isna())][['employee_id']].sort_values(by = 'employee_id')