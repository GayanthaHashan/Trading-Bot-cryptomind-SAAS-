
import pandas as pd
import numpy as np

def analyze_technicals(df):
    # df has columns: open, high, low, close, volume
    close = df['close']

    # EMA 20, 50 using pandas ewm (no pandas-ta needed)
    df['ema20'] = close.ewm(span=20, adjust=False).mean()
    df['ema50'] = close.ewm(span=50, adjust=False).mean()

    # RSI 14 manual
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(com=13, adjust=False).mean()
    avg_loss = loss.ewm(com=13, adjust=False).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    df['rsi'] = rsi

    # MACD 12,26,9 manual
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    df['MACD_12_26_9'] = macd_line
    df['MACDs_12_26_9'] = signal_line

    last = df.iloc[-1]
    prev = df.iloc[-2]

    patterns = []
    # Bullish Engulfing
    try:
        if prev['close'] < prev['open'] and last['close'] > last['open'] and last['close'] > prev['open']:
            patterns.append({"name":"Bullish Engulfing","confidence":0.84,"type":"bullish"})
        if prev['close'] > prev['open'] and last['close'] < last['open'] and last['close'] < prev['open']:
            patterns.append({"name":"Bearish Engulfing","confidence":0.84,"type":"bearish"})
    except:
        pass

    # EMA20 Breakout
    try:
        if last['close'] > last['ema20'] and prev['close'] < prev['ema20']:
            patterns.append({"name":"EMA20 Breakout","confidence":0.72,"type":"bullish"})
        if last['close'] < last['ema20'] and prev['close'] > last['ema20']:
            patterns.append({"name":"EMA20 Breakdown","confidence":0.72,"type":"bearish"})
    except:
        pass

    # Ascending Triangle
    try:
        if df['low'].iloc[-5:].is_monotonic_increasing:
            patterns.append({"name":"Ascending Triangle","confidence":0.71,"type":"bullish"})
    except:
        pass

    rsi_val = last['rsi'] if not pd.isna(last['rsi']) else 50

    return {
        "rsi": round(float(rsi_val), 2),
        "ema20": float(last['ema20']),
        "ema50": float(last['ema50']),
        "macd_signal": "bullish" if last['MACD_12_26_9'] > last['MACDs_12_26_9'] else "bearish",
        "macd": round(float(last['MACD_12_26_9']), 4),
        "macd_signal_line": round(float(last['MACDs_12_26_9']), 4),
        "patterns": patterns,
        "close": float(last['close'])
    }
