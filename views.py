from flask import Blueprint, render_template, send_file

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/pdf")
def pdf():
    return send_file('referat.pdf')

