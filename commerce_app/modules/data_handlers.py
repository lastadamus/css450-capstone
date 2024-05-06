import pandas as pd


def csv_to_df(path: str) -> pd.DataFrame:
    """Convert a CSVFile path to PD DataFrame"""
    return pd.read_csv(path)


def get_df_row(df: pd.DataFrame, id: str) -> pd.Series:
    """Gets a row from a dataframe by id: str"""
    return df.iloc[df[id]]


def insert_df_row(df: pd.DataFrame, new_rows: pd.DataFrame) -> pd.DataFrame:
    """Adds new rows by concat new_rows to df"""
    return pd.concat([df, new_rows], ignore_index=True)
