import pandas as pd
import re

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].apply(lambda x: bool(re.search(r'(^|\s)(DIAB1)', x, re.IGNORECASE)))]