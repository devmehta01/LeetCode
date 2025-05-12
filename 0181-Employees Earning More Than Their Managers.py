import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(employee, how='left', left_on='managerId', right_on='id')
    filtered_df = merged_df.query('salary_x > salary_y')
    result_df = pd.DataFrame({'Employee': filtered_df['name_x']})
    return result_df