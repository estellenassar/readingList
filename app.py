from flask import Flask, render_template, request
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

@app.route("/reviews", methods=["POST"])
def reviews():
	form_data = request.form
	book_input = form_data["book_title"]

	results = nyt_reviews(book_input)

	return render_template("reviews.html", titleresults=results)

def nyt_reviews(book_input):
	load_dotenv()
	api_key = os.getenv("NYT_API_KEY")
	
	endpoint = 'https://api.nytimes.com/svc/books/v3/reviews.json'
	payload = {"api-key" : api_key, "title":book_input}
	response = requests.get(endpoint, params=payload)

	json_data = response.json()

	return json_data["results"]

@app.route("/thankyou")
def thankyou():
	return render_template("thank-you.html")

def nyt_overview():
	load_dotenv()
	api_key = os.getenv("NYT_API_KEY")

	endpoint = "https://api.nytimes.com/svc/books/v3/lists/overview.json"
	payload = {"api-key" : api_key}
	response = requests.get(endpoint, params=payload)

	json_data = response.json()

	return json_data

@app.route("/fiction")
def fiction():
	
	json_data = nyt_overview()
	fiction_books = json_data['results']['lists'][0]['books']
	
	return render_template("fiction.html", bookresults=fiction_books)

@app.route("/nonfiction")
def nonfiction():

	json_data = nyt_overview()
	nonfiction_books = json_data['results']['lists'][1]['books']

	return render_template("non-fiction.html", bookresults=nonfiction_books)

@app.route("/business")
def business():

	json_data = nyt_overview()
	business_books = json_data['results']['lists'][13]['books']

	return render_template("business.html", bookresults=business_books)

@app.route("/miscellaneous")
def miscellaneous():

	json_data = nyt_overview()
	miscellaneous_books = json_data['results']['lists'][6]['books']

	return render_template("miscellaneous.html", bookresults=miscellaneous_books)

if  __name__  ==  "__main__":
	app.run(debug=True)