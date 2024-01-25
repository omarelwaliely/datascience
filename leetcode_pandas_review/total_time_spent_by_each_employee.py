import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees[['event_day','emp_id','total_time']].rename(columns = {'event_day': 'day'})
    return result.groupby(['day','emp_id'])['total_time'].sum().reset_index()