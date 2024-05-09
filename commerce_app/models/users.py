from models import models

base_user = models.BaseUser()
print(base_user)


class User(models.BaseUser):
    def __init__(self) -> None:
        super().__init__()
        self.created_date = ""
        self.address = ""
        self.email_address = ""
        self.first_name = ""
        self.last_name = ""
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
            self.first_name = response["first_name"]
            self.last_name = response["last_name"]
            self.user_name = response["user_name"]
        except Exception as e:
            print("key error likely")
            raise e

    def create_user(
        self,
        id: str,
        username: str,
        physical_address: str,
        password: str,
        email_address: str,
        first_name: str,
        last_name: str,
        created_date: str,
    ):
        self.id = id
        self.user_name = username
        self.address = physical_address
        self.password = password
        self.email_address = email_address
        self.first_name = first_name
        self.last_name = last_name
        self.created_date = created_date
        return {
            "user": {
                "id": self.id,
                "user_name": self.user_name,
                "password": self.password,
                "email_address": self.email_address,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "physical_address": self.address,
                "created_date": self.created_date,
            }
        }
