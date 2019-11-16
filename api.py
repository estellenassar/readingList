from flask import Flask, render_template
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

load_dotenv()
api_key = os.getenv("NYT_API_KEY")
print "\n" + api_key + "\n"

endpoint = "https://api.nytimes.com/svc/books/v3/lists/overview.json"
payload = {"api-key" : api_key}
response = requests.get(endpoint, params=payload)

json_data = response.json()

print json_data['results']['lists'][0]['display_name']
print json_data['results']['lists'][1]['display_name']
print json_data['results']['lists'][6]['display_name']
print json_data['results']['lists'][13]['display_name']
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
# print response.url
# print response.status_code
# print response.headers["content-type"]