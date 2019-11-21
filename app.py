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
	book_title = form_data["book_title"]
	book_author = form_data["book_author"]

	book_input = (["book_title", book_title],["book_author", book_author])

	if not book_input[1][1]:
		user_data = book_title
	elif not book_input[0][1]:
		user_data = book_author
	else:
		user_data = book_title + ' by ' + book_author

	results = nyt_reviews(book_input)

	return render_template("reviews.html", titleresults=results, search_data=user_data)

def nyt_reviews(book_input):
	load_dotenv()
	api_key = os.getenv("NYT_API_KEY")
	
	endpoint = 'https://api.nytimes.com/svc/books/v3/reviews.json'

	if not book_input[1][1]:
		payload = {"api-key" : api_key, "title": book_input[0][1]}
		print 1
	elif not book_input[0][1]:
		payload = {"api-key" : api_key, "author": book_input[1][1]}
		print 2
	else:
		payload = {"api-key" : api_key, "title": book_input[0][1], "author": book_input[1][1]}
		print 3

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

@app.route("/massmarket")
def massmarket():

	json_data = nyt_overview()
	mass_market_books = json_data['results']['lists'][15]['books']

	return render_template("mass-market.html", bookresults=mass_market_books)

if  __name__  ==  "__main__":
	app.run(debug=True)