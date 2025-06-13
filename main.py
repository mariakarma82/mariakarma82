from sentiment_utils import get_news_sentiment
from price_utils import get_btc_price_change
import datetime

if __name__ == "__main__":
    sentiment_score = get_news_sentiment()
    price_change = get_btc_price_change(hours=6)

    print(f"[{datetime.datetime.now()}] Sentiment Score: {sentiment_score:.3f}, Price Change: {price_change:.2f}%")

    if sentiment_score > 0.3 and price_change < -0.5:
        print("🚨 Warning: Positive sentiment but price is falling. Potential manipulation or lag!")
    elif sentiment_score < -0.3 and price_change > 0.5:
        print("🚨 Warning: Negative sentiment but price is rising. Market acting irrationally.")
    else:
        print("✅ Market sentiment aligns with price action.")

