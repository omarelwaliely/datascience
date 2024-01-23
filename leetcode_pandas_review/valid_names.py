import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r'\b[A-Za-z][A-Za-z0-9._-]*@leetcode\.com\b'
    return users[users['mail'].str.fullmatch(regex)]