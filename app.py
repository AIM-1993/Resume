import os
from flask import Flask, render_template, redirect, url_for, request, send_file, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# app.config.from_pyfile('config.py')
# db = SQLAlchemy(app)
bootstrap = Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("resume.html")


@app.route("/<filename>", methods=["GET"])
def download(filename):
    directory = os.getcwd()  # 假设在当前目录
    return send_from_directory(directory, filename, as_attachment=True)



if __name__ == "__main__":
    from werkzaug.contrib.fixers import ProxyFix
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()
