import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders,left_on = 'id', right_on = 'customerId', how = 'outer')
    return merged[merged['id_y'].isnull()][['name']].rename(columns={"name": "Customers"})