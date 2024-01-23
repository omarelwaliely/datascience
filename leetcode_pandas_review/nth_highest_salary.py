import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.sort_values(by = ['salary'], ascending = False)[['salary']].drop_duplicates(subset=['salary']).rename(columns = {'salary': f'getNthHighestSalary({N})'})
    if N >0 and N <= len(employee):
        return employee.iloc[[N - 1]]
    else:
        nullTable = pd.DataFrame(columns=[f'getNthHighestSalary({N})'])
        return nullTable._append({f'getNthHighestSalary({N})': None}, ignore_index =True)