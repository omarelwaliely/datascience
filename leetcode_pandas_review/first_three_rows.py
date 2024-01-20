import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    """
    some more ways:
    return employees.head(3)
    return employees.loc[0:2]
    """
    return employees[:3]