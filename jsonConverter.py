# ---------------------JSON libraries------------------------
import json
from json import JSONDecodeError


# -----------Parse JSON to Python Object-----------
def parseJSON(jsonStr):
    pythonData = json.loads(jsonStr)
    return pythonData

# ----------------Serialize to JSON------------------
def serializeJSON(scoreResponse, magnitudeResponse):
    # define Python object
    pythonData = {
        "score": scoreResponse,
        "magnitude": magnitudeResponse
    }
    # Exception Handler to encode to json
    try:  
        # ->OPTION 1: serialize to json as a string
        jsonStr = json.dumps(pythonData, indent=4)
        # print(jsonStr)
        return jsonStr
        # ->OPTION 2: serialize to json to separate file
        # json.dump(pythonData, open("nlpSentimentResponse.json","w"))
    except JSONDecodeError as err:
        print("Whoops, json encoder error:")
        print(err.msg)
        print(err.lineno, err.colno)

# ----------------Serialize to JSON(Special case)-------------
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
