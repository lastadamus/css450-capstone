from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return render_template("index.html")
    elif request.method == "GET":
        return render_template("index.html")


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True, ssl_context="adhoc")
