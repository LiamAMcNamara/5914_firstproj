# Sources:
# https://www.geeksforgeeks.org/get-post-requests-using-python/
# https://cloud.ibm.com/apidocs/natural-language-understanding
# importing the requests library
import requests

# prompt user for web article
print("Enter a URL to assess:")
user_url = str(input())

# defining the api-endpoint - URL provided by IBM cloud
API_ENDPOINT = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/e541f325-33c5-43d7-bb28-99c5a28df033/v1/analyze?version=2019-07-12"

# API Key - Provided by IBM cloud
API_KEY = "Z8NuVq4FEI4qCKFx2N0xMyKk0J02trGrmRSGh7lO-9wG"

# request headers
header = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# data to be sent to api
data = {"url": user_url,
        "features": {
            "sentiment": {},
            "categories": {},
            "concepts": {},
            "entities": {},
            "keywords": {}
        }
}

# sending POST request and saving response as response object
r = requests.post(url=API_ENDPOINT, headers=header, params=data, auth = ('apikey', API_KEY))
print(r.text)

#TODO: Do something (cool) with response
