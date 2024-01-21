import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(columns = "city", index = "month", values = 'temperature', aggfunc = 'max')