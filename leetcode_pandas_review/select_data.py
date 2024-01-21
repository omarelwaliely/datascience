import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    another way:
    return students[students["student_id"] == 101][['name'],['age']]]
    """
    return students[students["student_id"] == 101].drop(columns = ['student_id'])
    