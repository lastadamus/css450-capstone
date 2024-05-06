from models import models

base_user = models.BaseUser()
print(base_user)


class User(models.BaseUser):
    def __init__(self) -> None:
        super().__init__()
        self.created_date = ""
        self.address = {"": ""}
        self.email_address = ""
        self.f_name = ""
        self.l_name = ""
        self.user_name = ""

    def get_user(self, id: str):
        """Returns User attributes from back-end

        Args:
            id (str): user id required to fetch user

        Raises:
            e: any error associated with the request / response
        """
        self.id = id

        try:
            response = "this will return a dict of query result"
        except Exception as e:
            print("request event syntax error likely")
            raise e

        try:
            self.created_date = response["created_date"]
            self.address = response["address"]
            self.email_address = response["email_address"]
            self.f_name = response["f_name"]
            self.l_name = response["l_name"]
            self.user_name = response["user_name"]
        except Exception as e:
            print("key error likely")
            raise e

    def create_user(self, **args):
        self.id = args["id"]
        self.user_name = args["user_name"]
        self.address = args["address"]
        self.email_address = args["email_address"]
        self.f_name = args["f_name"]
        self.l_name = args["l_name"]
        self.created_date = args["created_date"]
        return {
            "user": {
                "id": self.id,
                "user_name": self.user_name,
                "email_address": self.email_address,
                "f_name": self.f_name,
                "l_name": self.l_name,
                "address": self.address,
                "created_date": self.created_date,
            }
        }
