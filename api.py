from flask import Flask, render_template
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

load_dotenv()
api_key = os.getenv("NYT_API_KEY")

endpoint = "https://api.nytimes.com/svc/books/v3/reviews.json"
payload = {"api-key" : api_key, "author": 'Lee Child'}
response = requests.get(endpoint, params=payload)

json_data = response.json()

print json_data

print json_data['results'][0]['book_title']
print json_data['results'][0]['book_author']
print json_data['results'][0]['summary']
print json_data['results'][0]['url']

# print response.url
# print response.status_code
# print response.headers["content-type"]