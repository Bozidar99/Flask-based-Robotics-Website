from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template ("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def news():
    return render_template("about.html")

@app.route("/team")
def article():
    return render_template("team.html")

