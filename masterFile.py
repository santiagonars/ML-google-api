# --------------------Main Local Libraries---------------------
import io
import os
# ---------------------API Libraries---------------------
from flask import Flask
from flask import request,jsonify
from flask_restful import Api, Resource, reqparse
# ------------------Web Scraping Libraries-------------------
import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup
# ----------------------JSON libraries------------------------
import json
from json import JSONDecodeError
# ---------Natural Language Processing Libraries (NLP)--------
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# app = Flask(__name__)
# api = Api(app)
url = str()

class Data (Resource):
    
    def __init__(self):
        self.result = Resource

    #POST method that gets the information that I need
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("message")
        #parser.add_argument(self.result)
        args = parser.parse_args()
        # result = parser
        print('Alejandro')
        #print(self.result)
        print(args)
        # print(result)
        return args, 201

    def get(self):
        pass


url = "https://www.vice.com/en_us/article/59nyjq/another-republican-senator-who-snubbed-trump-could-be-in-trouble"

# ----------Make Request to Scrape URL----------
def httpRequest():
    # Use requests to issue a standard HTTP GET 
    try:
        result = requests.get(url ,timeout=10)
        # raise_for_status will throw an exception if an HTTP error
        result.raise_for_status
        print(result)
        # call web scraping function and pass result from request
        webScrapeURL(result)
    except HTTPError as err:
        print("Error: {0}".format(err))
    except Timeout as err:
        print("Request time out {0}".format(err))
    
# ------------Extract and Clean Text-----------
def webScrapeURL(result):
    html_code = result.content
    # web scrape hmtl
    soup = BeautifulSoup(html_code, 'html.parser')
    # Get Text inside paragraph tags
    extractedText = str()
    for p_tag in soup.find_all('p'): # Same but for paragraph tags
            textFound = p_tag.text
            extractedText += textFound
    # print(extractedText)
    nlpSentimentCall(extractedText)

# -----Load API Key to Access Google Cloud Platform--------
def apiAccess():
    #***IMPORTANT: make sure JSON file for service account key name is correct & that it's inside the authPath directory
    serviceKey = "debias-253616-2ce80c5caea0.json" # NLP key
    with open(serviceKey, 'r') as myfile:
        json_authCred=myfile.read()
        # print(json_authCred)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceKey
    # print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

# ------------NATURAL LANGUAGE API Call-----------
def nlpSentimentCall(extractedText):
    # Instantiates a client
    client = language.LanguageServiceClient()
    # Argument 1: The text to analyze
    text = extractedText
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Detects the sentiment of the text
    response = client.analyze_sentiment(document=document).document_sentiment
    # print('Text: {}'.format(text))
    # print(response.score)
    # print(response.magnitude)
    # call function to evaluate sentiment analysis results
    sentimentEvalResponse(response.score, response.magnitude)
    
# --------Evaluation of NLP Sentiment Analysis-------
def sentimentEvalResponse(score, magnitude):
    evaluation = str()
    # Low emotion
    if magnitude < 3.0: 
        if (score <= 0.1) and (score >= -0.1): #score close to 0
            evaluation = "Impartial"
        elif (score > 0.1):  
            evaluation = "Favorable Neutral"
        else: # score is less than -0.1
            evaluation = "Unfavorable Neutral"
    # High emotion
    else:
        if (score <= 0.1) and (score >= -0.1):
            evaluation = "Mixed Views with Emotions"
        elif score > 0.1:
            evaluation = "Highly Favorable"
        else: 
            evaluation = "Highly Unfavorable"
    # call function to serialize final data to JSON 
    convertToJSON(evaluation, score, magnitude)

# -----------Parse JSON to Python Object-----------
def parseJSON(jsonStr):
    global url
    data = json.loads(jsonStr)
    # print(data['url'])
    url = data['url']

# ----------------Serialize to JSON------------------
def convertToJSON(evaluation, scoreResponse, magnitudeResponse):
    # define Python object
    pythonData = {
        "evaluation": evaluation,
        "score": scoreResponse,
        "magnitude": magnitudeResponse
    }
    # Exception Handler to encode to json
    try:  
        # ->OPTION 1: serialize to json as a string
        evalJSONresponse = json.dumps(pythonData, indent=4)
        print(evalJSONresponse)
        # ->OPTION 2: serialize to json to separate file
        # json.dump(pythonData, open("nlpSentimentResponse.json","w"))
    except JSONDecodeError as err:
        print("Whoops, json encoder error:")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == '__main__':
    # api.add_resource(Data, "/processing")
    # app.run(debug=True)
    
    apiAccess()
    httpRequest()
    