import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup = person.loc[person.duplicated('email')==True]
    return dup[['email']].drop_duplicates(keep='first')