from flask import Flask, render_template
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

app = Flask("readingList")


@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/start")
def other_page():
	return render_template("start.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/team")
def team():
	return render_template("team.html")

@app.route("/feedback")
def feedback():
	return render_template("feedback.html")

@app.route("/thankyou")
def thankyou():
	return render_template("thank-you.html")

app.run(debug=True)