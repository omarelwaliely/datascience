import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return department.pivot_table(values = 'revenue', index = 'id', columns = 'month').reindex(columns = months).rename(columns = lambda x: x+"_Revenue").reset_index()