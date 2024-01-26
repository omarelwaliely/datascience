import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if len(orders) ==0:
        return orders[['customer_number']]
    final = orders.groupby('customer_number')['order_number'].count().reset_index()
    return pd.DataFrame([final.loc[final['order_number'].idxmax()]])[['customer_number']]