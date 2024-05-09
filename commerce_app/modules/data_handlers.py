import pandas as pd


def csv_to_df(path: str) -> pd.DataFrame:
    """Convert a CSVFile path to DataFrame"""
    return pd.read_csv(path)


def df_to_csv(df: pd.DataFrame) -> str:
    """Convert DataFrame to csv"""
    return df.to_csv(path_or_buf="df_csv.csv", index=False)


def get_df_row(df: pd.DataFrame, header: str, id: str) -> pd.Series:
    """Gets a row from a dataframe by id: str"""
    return df.loc[df[header] == id]


def insert_df_row(df: pd.DataFrame, new_rows: pd.DataFrame) -> pd.DataFrame:
    """Adds new rows by concat new_rows to df"""
    return pd.concat([df, new_rows], ignore_index=True)


def csv_database_validation(username: str, password: str):
    """Allows authentication against the dummy CSV database file

    Args:
        id (str): User UUID
        username (str): username
        password (str): user password

    Returns:
        True if both credentials are valid
        False if either credential is invalid
        False if the ID does not exist in the database
    """
    database: pd.DataFrame = csv_to_df(
        path="/Users/justin/css450-capstone/css450-capstone/df_csv.csv"
    )
    try:
        df_row = get_df_row(df=database, header="user_name", id=username)
        if not df_row.empty:
            if df_row.iloc[0]["user_name"] == username:
                print(df_row["user_name"])
                if df_row.iloc[0]["password"] == password:
                    print(df_row["password"])
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except Exception as e:
        raise (e)


if __name__ == "__main__":
    print(
        csv_database_validation(
            username="usertest100",
            password="email",
        )
    )
