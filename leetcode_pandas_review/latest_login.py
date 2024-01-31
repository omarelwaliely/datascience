import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    return logins[logins['time_stamp'].dt.year == 2020].sort_values(by = "time_stamp").drop_duplicates(keep = 'last', subset = 'user_id').rename(columns = {'time_stamp':'last_stamp'})