# -------------------Main Local Libraries--------------------
import io
import os
# ------------------Web Scraping Libraries-------------------
import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup
# ----------------------NOTES------------------------------
# TODO: implement imageScrapeURL() capability

# ----------Make Request to Retrieve all URL----------
def httpGetRequest(url):
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
def textScrapeURL(rawtext):
    html_code = rawtext.content
    # webscrape hmtl
    soup = BeautifulSoup(html_code, 'html.parser')
    # save text inside <paragraph> tags
    extractedText = str()
    for p_tag in soup.find_all('p'): # Same but for paragraph tags
            textFound = p_tag.text
            extractedText += textFound
    # print(extractedText)
    return extractedText

# ------------Extract and Clean Images-----------
def imageScrapeURL(result):
    pass
    html_code = result.content
    # webscrape hmtl
    soup = BeautifulSoup(html_code, 'html.parser')
    # TODO: save image URLs in <image> tags
    extractedImageURL = str()

# call for help in using functions
def funchelp():
    print('''
    Required libraries:
    - requests
    - bs4
    #---------------------------
    Function:
    httpGetRequest(url)

    Inputs:
    - Arg #1: url = url link (string)

    Outputs:
    - result = Raw text of url link (string)

    Description:
    - Makes a GET request and retrieves all raw text from url link 
    #---------------------------
    Function:
    textScrapeURL(rawtext)

    Inputs:
    - Arg #1: rawtext = all raw keywords from a url link (string)

    Outputs:
    - extractedText = clean text extracted paragraph tags (string)

    Description:
    - Web scrapes raw text for html, and then extracts text within paragraph tags
    #---------------------------
    ''')


if __name__ == 'KeywordExtraction':
    pass


