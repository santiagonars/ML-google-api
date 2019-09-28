# --------------------STEPS:------------------------------
# ---->>> NLP Configuration Setup:
# STEP 1: Activate Google Cloud Platform account
# STEP 2: pip3 install --upgrade google-cloud-language
# STEP 3:Enable NLP API:
#    -> https://console.cloud.google.com/apis/library/language.googleapis.com?q=natural&id=223648f2-2e7c-4acd-b0ca-782f9021a541&project=ardent-oven-253616
# STEP 4: Create API key  and store locally to access NLP API
# --------------------NOTES:------------------------------
# NOTE: 

# --------------------BUGS:------------------------------
# BUG: 

import io
import os
import json
from json import JSONDecodeError

# ----------Imports the Google Cloud NLP API----------
# from google.cloud import vision
# Natural Language Processing Libraries (NLP)
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


def apiAccess():
    # ---------Load API Key to Access Google Cloud Platform----------
    #***IMPORTANT: make sure JSON file for service account key name is correct & that it's inside the authPath directory
    #serviceKey = "CloudVision-sandbox-366681a0e85d.json"  # Cloud Vision key
    #print("Service Key= " + serviceKey)
    serviceKey = "debias-253616-bd2728a1c781.json" # NLP key
    with open(serviceKey, 'r') as myfile:
        json_authCred=myfile.read()
        # print(json_authCred)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceKey
    # print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])


# ------------NATURAL LANGUAGE API Call-----------
def nlpSentimentCall():
    # Instantiates a client
    client = language.LanguageServiceClient()

    # Argument 1: The text to analyze
    text = "The investigation into Donald Trump’s promise to a foreign leader, which shocked a member of the intelligence community into making a complaint, relates to Ukraine, according to numerous media outlets.The New York Times and ABC both confirmed the involvement of Ukraine, first reported by the Washington Post on Thursday night.The complaint was made two weeks after Trump spoke to newly-elected Ukrainian President Volodymyr Zelensky, a former comedian, in late July, where the leaders discussed improving U.S.-Ukraine relations by boosting investigations into corruption."
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    # Argument 2:(OPTIONAL FOR NOW) Encoding type -> Available values: NONE, UTF8, UTF16, UTF32
    #encoding_type = enums.EncodingType.UTF8

    # Detects the sentiment of the text
    response = client.analyze_sentiment(document=document).document_sentiment
    # print('Text: {}'.format(text))
    # print(response.score)
    # print(response.magnitude)

    convertToJSON(response.score, response.magnitude)
    

def convertToJSON(scoreResponse, magnitudeResponse):
    # define Python object
    pythonData = {
        "score": scoreResponse,
        "magnitude": magnitudeResponse
    }
    # Exception Handler to encode to json
    try:  
        # ->OPTION 1: serialize to json as a string
        jsonStr = json.dumps(pythonData, indent=4)
        print(jsonStr)
        # ->OPTION 2: serialize to json to separate file
        json.dump(pythonData, open("nlpSentimentResponse.json","w"))
    except JSONDecodeError as err:
        print("Whoops, json encoder error:")
        print(err.msg)
        print(err.lineno, err.colno)


if __name__ == '__main__':
    apiAccess()
    nlpSentimentCall()
