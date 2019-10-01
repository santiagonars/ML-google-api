# -------------------Main Local Libraries--------------------
import io
import os
# ---------------------JSON libraries------------------------
import json
from json import JSONDecodeError
# ------------------Web Scraping Libraries-------------------
import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup
# ----------------------NOTES------------------------------
# NOTE: 


url = "https://www.vice.com/en_us/article/59nyjq/another-republican-senator-who-snubbed-trump-could-be-in-trouble"

# ----------Make Request to Retrieve all URL----------
def httpGetRequest():
    # Use requests to issue a standard HTTP GET 
    try:
        result = requests.get(url ,timeout=10)
        # raise_for_status will throw an exception if an HTTP error
        result.raise_for_status
        print(result)
        # call web scraping function and return result from request
        return result
    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request time out {0}".format(err))
    
# ------------Extract and Clean Text-----------
def textScrapeURL(result):
    html_code = result.content
    # webscrape hmtl
    soup = BeautifulSoup(html_code, 'html.parser')
    # save text inside <paragraph> tags
    extractedText = str()
    for p_tag in soup.find_all('p'): # Same but for paragraph tags
            textFound = p_tag.text
            extractedText += textFound
    print(extractedText)

# ------------Extract and Clean Images-----------
def imageScrapeURL(result):
    pass
    html_code = result.content
    # webscrape hmtl
    soup = BeautifulSoup(html_code, 'html.parser')
    # TODO: save image URLs in <image> tags
    extractedImageURL = str()

# -----------Parse JSON to Python Object-----------
def parseJSON(jsonStr):
    global url
    data = json.loads(jsonStr)
    # print(data['url'])
    url = data['url']

# ----------------Serialize to JSON------------------
def convertToJSON(evaluation, scoreResponse, magnitudeResponse):
    # # define Python object
    # pythonData = {
    #     "evaluation": evaluation,
    #     "score": scoreResponse,
    #     "magnitude": magnitudeResponse
    # }
    pythonData = {
        # "key", value
    }
    # Exception Handler to encode to json
    try:  
        # ->OPTION 1: serialize to json as a string
        JSONdata = json.dumps(pythonData, indent=4)
        print(JSONdata)
        # ->OPTION 2: serialize to json to separate file
        # json.dump(pythonData, open("jsonData.json","w"))
    except JSONDecodeError as err:
        print("Whoops, json encoder error:")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == '__main__':
    urlData = httpGetRequest()
    textScrapeURL(urlData)


