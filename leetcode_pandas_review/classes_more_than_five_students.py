import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = courses.groupby('class').count().reset_index()
    return result[result['student'] >= 5][['class']]