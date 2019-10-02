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
def textScrapeURL(result):
    html_code = result.content
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

    
if __name__ == 'KeywordExtraction':
    pass


