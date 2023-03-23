from flask import Flask, render_template, request
app = Flask(__name__)
from extractors.jobscrapper import extract_jobs

@app.route('/')
def hello_world():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    result = extract_jobs(keyword)
    return render_template("search.html", keyword = keyword, result = result )