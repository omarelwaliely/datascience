import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.pivot_table(values = ['lead_id','partner_id'], index = ['date_id','make_name'],aggfunc="nunique").reset_index().rename(columns = {'lead_id': 'unique_leads', 'partner_id':'unique_partners'})