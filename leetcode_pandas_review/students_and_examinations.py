import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    attended_exams = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    all_combinations = pd.merge(students.assign(key=1), subjects.assign(key=1), on='key').drop('key', axis=1)
    result = pd.merge(all_combinations, attended_exams, how='left', on=['student_id', 'subject_name']).sort_values(by=['student_id', 'subject_name']).reset_index(drop=True)[['student_id', 'student_name', 'subject_name', 'attended_exams']]
    result['attended_exams'] = result['attended_exams'].fillna(0) 
    return result