from flask import Flask, render_template, request
app = Flask(__name__)
from extractors.remoteok import extract_jobs
from extractors.weworkremotely import extract_jobs1

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    reok = extract_jobs(keyword)
    wework = extract_jobs1(keyword)
    return render_template("search.html", keyword = keyword, reok = reok, wework = wework )