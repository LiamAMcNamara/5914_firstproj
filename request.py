# Sources:
# https://www.geeksforgeeks.org/get-post-requests-using-python/
# https://cloud.ibm.com/apidocs/natural-language-understanding
# importing the requests library
import requests
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# prompt user for web airticle
print("Enter a URL to assess:")
user_url = str(input())

# defining the api-endpoint - URL provided by IBM cloud
API_ENDPOINT = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/e541f325-33c5-43d7-bb28-99c5a28df033/v1/analyze?version=2019-07-12"

# API Key - Provided by IBM cloud
API_KEY = "Z8NuVq4FEI4qCKFx2N0xMyKk0J02trGrmRSGh7lO-9wG"

# request headers
header = {'Content-Type': 'application/json', 'Accept': 'application/json'}

# data to be sent to api
data = {
    "url": user_url,
    "features": {
        "sentiment": {},
        "categories": {},
        "concepts": {},
        "entities": {},
        "keywords": {
            #"Hail Mary": True,
        }
    }
}

# sending POST request and saving response as response object
r = requests.post(url=API_ENDPOINT,
                  headers=header,
                  params=data,
                  auth=('apikey', API_KEY))
print(type(r.text))

#TODO: Do something (cool) with response

for kw in r.json()["keywords"]:
    print("%f\t%d\t%s" % (kw["relevance"], kw["count"], kw["text"]))

wordCount = {}

for kw in r.json()["keywords"]:
    text = kw["text"]
    count = kw["count"]
    relevance = kw["relevance"]

    for word in text.split(" "):
        word = word.lower()
        if (word in wordCount):
            wordCount[word] += count * relevance
        else:
            wordCount[word] = count * relevance

for prep in ["in", "of", "and", "or", "if", "so", "on"]:
    if prep in wordCount:
        wordCount.pop(prep)

wordsorted = sorted(wordCount.items(), key=lambda item: item[1])
wordsorted.reverse()

print(wordsorted[:10])

for word in wordsorted[10:]:
    wordCount.pop(word[0])

wc = WordCloud()
wc.generate_from_frequencies(wordCount)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()