# If you find any parts of this code useful in any of the libraries  please add:
'''
Cite:
Norena Santiago, ML-google-api: nlp_sentiment-analysis, (2020), 
GitHub repository, https://github.com/santiagonorena/ML-google-api
'''

# -------------------Modules--------------------
import jsonConverter
import TextScraper
import SentimentAnalysisNLP


def main():
    #test #1:
    # url = "https://www.vice.com/en_us/article/59nyjq/another-republican-senator-who-snubbed-trump-could-be-in-trouble"
    #test #2:
    # url = "https://www.buzzfeednews.com/article/zoetillman/trump-administration-census-settlement"
    #test #3:
    url = "https://www.foxnews.com/politics/biden-vp-hopeful-bass-regrets-past-castro-comment"

    #use for help => print(TextScraper.funchelp())
    urlData = TextScraper.httpGetRequest(url)
    extractedText = TextScraper.textScrapeURL(urlData)
    # print(extractedText)

    score, magnitude = SentimentAnalysisNLP.nlpSentimentCall(extractedText)
    jsonData = jsonConverter.serializeJSON(score, magnitude)
    print(jsonData)

if __name__ == '__main__':
    main()
