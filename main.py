from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index_view():
    return render_template("index.html")
