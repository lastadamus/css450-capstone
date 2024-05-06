from modules.data_handlers import csv_to_df, get_df_row, insert_df_row
from models.users import User
import pandas as pd

CSVPATH: str = "test_files/csv_test.csv"

"""Create an empty df_template for testing, then create a df with template"""
df_template = csv_to_df(path=CSVPATH)
df = df_template

"""Create a new user Object by setting attributes"""
new_user = User()
user = new_user.create_user(
    id="1",
    email_address="email@none",
    user_name="username",
    f_name="first",
    l_name="last",
    address="address",
    created_date="yyyy-mm-dd",
)

"""Pass the user attributes into a DataFrame object as :new_rows:"""
new_rows = pd.DataFrame(
    {
        "id": new_user.id,
        "email_address": new_user.email_address,
        "user_name": new_user.user_name,
        "f_name": new_user.f_name,
        "l_name": new_user.l_name,
        "address": new_user.address,
        "created_date": new_user.created_date,
    },
    index=[0],
)

"""Join the original df and the new rows together, adding new rows to original"""
df = pd.concat([df, new_rows], ignore_index=True)
print(df)
