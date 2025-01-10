from flask import Flask, render_template, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "d6ad52c24926b2c98f099c76467bfbcc7c5eef8659916b6"
app.static_folder = "static"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["content"]
        return "{}".format(content)
    return render_template("index.html")
