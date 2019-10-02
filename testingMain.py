import KeywordExtraction
import SentimentAnalysisNLP


# url = "https://www.vice.com/en_us/article/59nyjq/another-republican-senator-who-snubbed-trump-could-be-in-trouble"
url = "https://www.buzzfeednews.com/article/zoetillman/trump-administration-census-settlement"

urlData = KeywordExtraction.httpGetRequest(url)
extractedText = KeywordExtraction.textScrapeURL(urlData)
print(extractedText)

SentimentAnalysisNLP.apiAccess()
score, magnitude = SentimentAnalysisNLP.nlpSentimentCall(extractedText)
jsonData = SentimentAnalysisNLP.convertToJSON(score, magnitude)
print(jsonData)


if __name__ == '__main__':
    pass