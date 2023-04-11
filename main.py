from flask import Flask, render_template, request

app = Flask(__name__)

with open("flag.txt", "r", encoding="utf-8") as f:
    flag = f.read()

@app.route("/", methods=["GET"])
def index_view():
    return render_template("index.html")

@app.route("/flag", methods=["GET", "POST"])
def flag_view():
    if request.method == "POST":
        pwd = request.form["passord"]
        if pwd == "heipådeg".replace("å", "aa").replace("d", "z"):
            return render_template("flag.html", flag=flag)
        else:
            return render_template("flag.html", feil="Passordet du oppga er ikke riktig.")
    else:
        return render_template("flag.html")