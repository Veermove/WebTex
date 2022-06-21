from flask import Blueprint, render_template, send_file, send_from_directory, request
from core import save_and_compile, change_preset, compile_saved
import os

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

@views.route("/starter", methods=['GET'])
def starter_code():
    default = 'essay'
    args = request.args
    if "preset" in args:
        default = args["preset"]
    
    change_preset(default)
    compile_saved()
    return get_default_text()

@views.route('/submit', methods=['POST'])
def submit():
    return helper(request.form['text'])

def helper(text):
    save_and_compile(text)
    return home()

@views.route('/def_text', methods=['GET'])
def get_default_text():
    with open('resources/t_file.tex', 'r') as default:
        return default.read()
    
    return 500, "Coud not open t_file.tex"


@views.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(os.getcwd() + '/resources', filename)

@views.after_request
def apply_caching(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
