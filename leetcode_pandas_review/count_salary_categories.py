import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def find_type(x):
        if x<20000:
            return "Low Salary"
        elif x>=20000 and x<= 50000:
            return "Average Salary"
        else:
            return "High Salary"

            
    accounts['type'] = accounts["income"].apply(find_type)
    all_types = ["Low Salary", "Average Salary", "High Salary"]
    final = accounts['type'].value_counts().reset_index()
    final = final.rename(columns = {'type': 'category', 'count': 'accounts_count'})
    missing_types = list(set(all_types) - set(final['category']))
    missing_counts = pd.DataFrame({'category': missing_types, 'accounts_count': [0] * len(missing_types)})
    result = pd.concat([final, missing_counts]).reset_index(drop=True)
    
    return result