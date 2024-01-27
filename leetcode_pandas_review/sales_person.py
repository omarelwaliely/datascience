import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = company[company['name'] == 'RED'].merge(orders, on = 'com_id').merge(sales_person, on = 'sales_id', how = 'right')
    return  res[res.isna().any(axis=1)][['name_y']].rename(columns = {'name_y':'name'})