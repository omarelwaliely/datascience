import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.sort_values(by = ['salary'], ascending = False)[['salary']].drop_duplicates(subset=['salary']).rename(columns = {'salary':'SecondHighestSalary'})
    if 2 <= len(employee):
        return employee.iloc[[1]]
    else:
        nullTable = pd.DataFrame(columns=[f'SecondHighestSalary'])
        return nullTable._append({f'SecondHighestSalary': None}, ignore_index =True)
    