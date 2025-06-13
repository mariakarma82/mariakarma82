import requests
from textblob import TextBlob

def get_news_sentiment():
    url = "https://cryptopanic.com/api/v1/posts/?auth_token=demo&currencies=BTC&public=true"
    response = requests.get(url)
    posts = response.json().get("results", [])

    total_polarity = 0
    for post in posts[:10]:
        title = post.get("title", "")
        analysis = TextBlob(title)
        total_polarity += analysis.sentiment.polarity

    return total_polarity / max(len(posts[:10]), 1)
