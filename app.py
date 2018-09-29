import os
from flask import Flask, render_template, redirect, url_for, request, send_file, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("resume.html")


@app.route("/<filename>", methods=["GET"])
def download(filename):
    directory = os.getcwd()
    return send_from_directory(directory, filename, as_attachment=True)


@app.route("/items/")
def items():
    return render_template("items.html")

if __name__ == "__main__":
    from werkzaug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
