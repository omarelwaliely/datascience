import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers_with_reports = employee[employee['managerId'].notnull()]
    report_counts = managers_with_reports.groupby('managerId').size().reset_index(name='directReports')
    result = report_counts[report_counts['directReports'] >= 5]
    result = result.merge(employee[['id', 'name']], left_on='managerId', right_on='id', how='inner')
    return result[['name']]