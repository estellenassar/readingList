from flask import Flask, render_template
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

# load_dotenv()
# api_key = os.getenv("NYT_API_KEY")

# book_input = (["book_title", ''],["author", 'Lee Child'])

# endpoint = "https://api.nytimes.com/svc/books/v3/reviews.json"

# if not book_input[1][1]:
#     payload = {"api-key" : api_key, "title": book_input[0][1]}
#     print 1
# elif not book_input[0][1]:
#     payload = {"api-key" : api_key, "author": book_input[1][1]}
#     print 2
# else:
#     payload = {"api-key" : api_key, "title": book_input[0][1], "author": book_input[1][1]}
#     print 3

# response = requests.get(endpoint, params=payload)

# json_data = response.json()

# print json_data

book_title = 'The Hidden History Of Burma'
author = 'Lee Child'

book_input = (["book_title", book_title],["author", author])

if not book_input[1][1]:
	user_data = book_title
elif not book_input[0][1]:
	user_data = author
else:
	user_data = book_title + ' by ' + author

print user_data

# print json_data['results'][0]['book_title']
# print json_data['results'][0]['book_author']
# print json_data['results'][0]['summary']
# print json_data['results'][0]['url']

# print response.url
# print response.status_code
# print response.headers["content-type"]