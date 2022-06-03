from flask import Blueprint, render_template, send_file
from requests import request
from commons import is_filename_ok

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/pdf")
def pdf():
    return send_file('resources/referat.pdf')

@views.route("/indexjs")
def indexjs():
    return send_file('templates/index.js')

@views.route("/cmp", methods=['POST'])
def compaile_and_send():
    if 'file' not in request.files:
        return 'File not found', 400

    file = request.files['file']

    if not file or not is_filename_ok(file.filename):
        return 'File is corrupted', 400

    compile(file)
    return 'Success!', 200
