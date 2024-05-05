from modules.data_handlers import csv_to_df, get_df_row, insert_df_row
from models.users import User
import pandas as pd

# CSVPath: test_files/csv_test.csv
CSVPATH: str = "test_files/csv_test.csv"

df_template = csv_to_df(path=CSVPATH)
# print(df_template)

new_user = User().create_user(
    id="1",
    email_address="email@none",
    user_name="username",
    f_name="first",
    l_name="last",
    address="address",
    created_date="yyyy-mm-dd",
)


new_rows = pd.DataFrame(
    new_user
    # {
    #     "id": new_user.id,
    #     "email_address": new_user.email_address,
    #     "user_name": new_user.user_name,
    #     "f_name": new_user.f_name,
    #     "l_name": new_user.l_name,
    #     "address": new_user.address,
    #     "created_date": new_user.created_date,
    # }
)
print(new_rows)
