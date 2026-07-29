
from datetime import datetime
def get_news_sentiment(symbol="BTCUSDT"):
    headlines=[{"title":f"{symbol} ETF sees $240M inflow","source":"CoinDesk","sentiment":0.82,"impact":"high"},{"title":"Fed holds rates, risk assets stable","source":"Reuters","sentiment":0.51,"impact":"medium"},{"title":"Whale accumulation detected on-chain","source":"On-chain","sentiment":0.74,"impact":"high"}]
    avg=sum(h['sentiment'] for h in headlines)/len(headlines)
    overall="bullish" if avg>0.6 else "bearish" if avg<0.4 else "neutral"
    return {"overall_score":round(avg,2),"overall_label":overall,"headlines":headlines,"timestamp":datetime.utcnow().isoformat()}
