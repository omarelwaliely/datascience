import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    res = employee.merge(bonus, how = 'left', on = 'empId')
    return res[(res['bonus']< 1000) | (res['bonus'].isna())][['name','bonus']]