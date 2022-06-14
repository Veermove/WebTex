from flask import Blueprint, render_template, send_file, request
from core import save_and_compile

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/pdf")
def pdf():
    return send_file('resources/t_file.pdf', conditional=False)

@views.route("/indexjs")
def indexjs():
    return send_file('templates/index.js')

@views.route("compileJson", methods=['POST'])
def compile_json_send():
    text = request.get_json()['text']
    
    save_and_compile(text)
    return render_template("index.html")


@views.route('/submit', methods=['POST'])
def submit():
    return helper(request.form['text'])

def helper(text):
    save_and_compile(text)
    return home()
