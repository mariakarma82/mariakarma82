import requests
import datetime

def get_btc_price_change(hours=6):
    end_time = int(datetime.datetime.utcnow().timestamp())
    start_time = end_time - hours * 3600

    url = (
        f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
        f"?vs_currency=usd&from={start_time}&to={end_time}"
    )
    response = requests.get(url)
    prices = response.json().get("prices", [])

    if not prices:
        return 0.0

    first = prices[0][1]
    last = prices[-1][1]
    return ((last - first) / first) * 100
