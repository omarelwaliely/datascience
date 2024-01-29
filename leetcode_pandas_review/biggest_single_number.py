import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:

    res = my_numbers['num'].drop_duplicates(keep = False)
    if res.empty:
        return pd.DataFrame({'num': [None]})
    else:
        return pd.DataFrame({'num': [max(res)]})