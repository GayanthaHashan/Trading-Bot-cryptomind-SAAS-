
import pandas as pd
def analyze_technicals(df):
    import pandas_ta as ta
    df['rsi']=ta.rsi(df['close'], length=14)
    df['ema20']=ta.ema(df['close'], length=20)
    df['ema50']=ta.ema(df['close'], length=50)
    macd=ta.macd(df['close'])
    df=pd.concat([df,macd], axis=1)
    last=df.iloc[-1]; prev=df.iloc[-2]
    patterns=[]
    if prev['close'] < prev['open'] and last['close'] > last['open'] and last['close'] > prev['open']:
        patterns.append({"name":"Bullish Engulfing","confidence":0.84,"type":"bullish"})
    if last['close'] > last['ema20'] and prev['close'] < last['ema20']:
        patterns.append({"name":"EMA20 Breakout","confidence":0.72,"type":"bullish"})
    if df['low'].iloc[-5:].is_monotonic_increasing:
        patterns.append({"name":"Ascending Triangle","confidence":0.71,"type":"bullish"})
    return {"rsi":round(float(last['rsi'] or 50),2),"ema20":float(last['ema20']),"ema50":float(last['ema50']),"macd_signal":"bullish" if last['MACD_12_26_9']>last['MACDs_12_26_9'] else "bearish","patterns":patterns,"close":float(last['close'])}
