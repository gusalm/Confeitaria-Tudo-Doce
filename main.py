from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/cardapio")
def cardapio():
    return render_template("cardapio.html")

@app.route("/contato")
def contatos():
    return render_template("contatos.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "abcdefg":
            if password == "1234567":
                return redirect(url_for('upload'))

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)