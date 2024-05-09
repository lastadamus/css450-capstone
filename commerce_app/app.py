import modules.data_handlers as dh
import models.users as u
import uuid
import pandas as pd
import datetime as dt
from flask import Flask, render_template, request, redirect, session, Response

app = Flask(__name__)
app.secret_key = "Test1234!1!"


@app.route("/", methods=["GET"])
def root_redirect():
    """Redirect users to login page if landing on root"""
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Prompt users to sign-in or register an account"""
    if request.method == "POST":
        session["credentials"] = request.form.to_dict()
        print(session["credentials"])
        return redirect("/auth")
    elif request.method == "GET":
        return render_template("login.html")


@app.route("/auth", methods=["GET"])
def auth():
    if not session["credentials"]["username"] or not session["credentials"]["password"]:
        return redirect("/login")
    if request.method == "GET":
        if session["credentials"]["username"] == "database_value":
            if session["credentials"]["password"] == "database_value":
                session["auth-key"] = uuid.uuid4()
                session["auth"] = True
                return redirect("/shopping_list")
        else:
            return {"status_code": 403, "message": "Invalid credentials entered"}


@app.route("/register", methods=["GET", "POST"])
def register():
    """Allows users to register a new account"""
    if request.method == "POST":
        user_profile = request.form.to_dict()
        del user_profile["conf_password"]

        user_profile["id"] = str(uuid.uuid4())
        user_profile["created_date"] = str(dt.datetime.now())

        try:
            new_user = u.User()
            user = new_user.create_user(
                id=user_profile["id"],
                email_address=user_profile["email_address"],
                username=user_profile["username"],
                password=user_profile["password"],
                first_name=user_profile["first_name"],
                last_name=user_profile["last_name"],
                physical_address=user_profile["physical_address"],
                created_date=user_profile["created_date"],
            )
            user_profile.clear()

            rows = pd.DataFrame(
                {
                    "id": user["user"].get("id"),
                    "email_address": user["user"].get("email_address"),
                    "password": user["user"].get("password"),
                    "user_name": user["user"].get("user_name"),
                    "first_name": user["user"].get("first_name"),
                    "last_name": user["user"].get("last_name"),
                    "address": user["user"].get("physical_address"),
                    "created_date": user["user"].get("created_date"),
                },
                index=[0],
            )
            df = dh.csv_to_df(
                "/Users/justin/css450-capstone/css450-capstone/df_csv.csv"
            )
            df_new = dh.insert_df_row(df=df, new_rows=rows)
            dh.df_to_csv(df=df_new)
        except Exception as e:
            print(e)
        return redirect("/login")
    elif request.method == "GET":
        return render_template("register.html")


@app.route("/shopping_list", methods=["GET", "POST"])
def shopping_list():
    """Allows users to interact with shopping list"""
    if not session:
        return redirect("/login")
    else:
        if (
            not session["auth"] == True
            and not session["auth-key"] == session["auth-key"]
        ):
            return redirect("/login")

    if request.method == "POST":
        return render_template("shopping_list.html")
    elif request.method == "GET":
        return render_template("shopping_list.html")


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True, ssl_context="adhoc")
