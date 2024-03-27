from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"


db =SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String)
    text = db.Column(db.String)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template ("index.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def news():
    return render_template("about.html")

@app.route("/blog", methods=["GET"])
def blog():

    message = Message.query.all()

    return render_template("blog.html", message=message)

@app.route("/add-message", methods=["POST"])
def add_message():

    username = request.form.get("username")
    text = request.form.get("text")

    message = Message(username = username, text = text)

    db.session.add(message)
    db.session.commit()

    return redirect("/blog")

@app.route("/delete/<msg_id>", methods=["GET"])
def delete_message(msg_id):

    message = Message.query.get(int(msg_id))
    
    db.session.delete(message)
    db.session.commit()

    return redirect("/blog")