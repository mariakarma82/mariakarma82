# 🧠 BTC Sentiment Mismatch Detector

A utility that compares real-time sentiment from crypto news (via CryptoPanic) against actual Bitcoin price movement (via CoinGecko).  
It detects mismatches — when the mood and market don’t align.

## 🚀 Features
- Pulls top 10 BTC news titles
- Analyzes sentiment using NLP (TextBlob)
- Compares against BTC price movement over past 6 hours
- Highlights potential market manipulation or lag

## 📦 Installation

```bash
git clone https://github.com/yourname/btc-sentiment-mismatch-detector.git
cd btc-sentiment-mismatch-detector
pip install -r requirements.txt
