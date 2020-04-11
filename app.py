from flask import Flask, render_template, request

from mbta_helper import find_stop_near


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")



@app.route("/mbta/", methods=["GET", "POST"])
def find_t():
    if request.method == "POST":
        a = str(request.form["a"])
        location, wheelchair = find_stop_near(a)

        if location:
            return render_template(
                "t_result.html", a=a, location=location, wheelchair=wheelchair
            )
        else:
            return render_template("find_t.html", error=True)
    return render_template("find_t.html", error=None)

