import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.merge(employee, how = 'left', left_on = 'managerId', right_on = 'id')
    return managers[managers['salary_x'] > managers['salary_y']][['name_x']].rename(columns = {'name_x':'Employee'})