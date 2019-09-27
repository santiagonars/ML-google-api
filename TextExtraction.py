# --------------------STEPS:------------------------------
# ---->>> Text Extraction from URL:
# STEP 1: pip3 install request
# STEP 2: pip3 install beautifulsoup4
# STEP 3:
# --------------------NOTES:------------------------------
# NOTE: 

# --------------------BUGS:------------------------------
# BUG: 

import io
import os
import requests
from requests.exceptions import HTTPError, Timeout
from bs4 import BeautifulSoup


url = "https://www.vice.com/en_us/article/59nyjq/another-republican-senator-who-snubbed-trump-could-be-in-trouble"

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
    

def webScrapeURL(result):
    html_code = result.content
    # 
    soup = BeautifulSoup(html_code, 'html.parser')

    stringToModify = ""
    for p_tag in soup.find_all('p'): # Same but for paragraph tags
            textFound = p_tag.text
            stringToModify += textFound
    print(stringToModify)


if __name__ == '__main__':
    httpRequest()


