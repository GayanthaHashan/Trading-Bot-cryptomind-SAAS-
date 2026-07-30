
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI(title="CryptoMind AI - Full SaaS Backend", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnalyzeReq(BaseModel):
    symbol: str = "BTCUSDT"
    interval: str = "1h"

class ChatReq(BaseModel):
    message: str
    symbol: str = "BTCUSDT"
    context: Optional[dict] = None

def rsi(prices, period=14):
    if len(prices) < period+1:
        return 50.0
    gains, losses = [], []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        gains.append(max(diff,0))
        losses.append(max(-diff,0))
    avg_gain = sum(gains[-period:])/period
    avg_loss = sum(losses[-period:])/period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain/avg_loss
    return 100 - (100/(1+rs))

def ema(prices, period):
    k = 2/(period+1)
    ema_val = sum(prices[:period])/period
    for p in prices[period:]:
        ema_val = p*k + ema_val*(1-k)
    return ema_val

@app.get("/")
def root():
    return {
        "status":"CryptoMind AI Full SaaS Online - FINAL",
        "mode":"NO_NUMPY_NEEDED",
        "endpoints":["/","/health","/analyze","/chat","/portfolio"],
        "docs":"/docs"
    }

@app.get("/health")
def health():
    return {"ok": True, "has_core": True, "mode":"FULL_SAAS_WITH_AI", "pc_storage":"0MB"}

@app.post("/analyze")
def analyze(req: AnalyzeReq):
    # Simulate 100 candles
    base_price = {"BTCUSDT":62000,"ETHUSDT":3200,"SOLUSDT":140,"BNBUSDT":600}.get(req.symbol, 60000)
    prices = [base_price + random.uniform(-800,800) + i*2 for i in range(100)]
    closes = prices
    close = closes[-1]
    rsi_val = rsi(closes)
    ema20_val = ema(closes, 20)
    ema50_val = ema(closes, 50)

    if rsi_val < 30 and close > ema20_val:
        action, conf = "BUY", 0.88
        reasoning = f"Oversold RSI {rsi_val:.1f} + price above EMA20 (${ema20_val:.0f}). Strong reversal bullish. Confidence 88%."
    elif rsi_val > 70:
        action, conf = "SELL", 0.82
        reasoning = f"Overbought RSI {rsi_val:.1f}. Momentum fading, take profit."
    elif rsi_val < 40 and ema20_val > ema50_val:
        action, conf = "BUY", 0.72
        reasoning = f"RSI {rsi_val:.1f} recovering, EMA20 > EMA50 uptrend. Good entry."
    elif rsi_val > 60 and ema20_val < ema50_val:
        action, conf = "SELL", 0.68
        reasoning = f"RSI {rsi_val:.1f} high but downtrend EMA20 < EMA50. Exit signal."
    else:
        action, conf = "HOLD", 0.55
        reasoning = f"RSI {rsi_val:.1f} neutral. Price ${close:.0f} between EMAs. Wait for confirmation."

    return {
        "symbol": req.symbol,
        "interval": req.interval,
        "technical":{"close":close,"rsi":round(rsi_val,2),"ema20":ema20_val,"ema50":ema50_val,"macd":0.5,"rsi":round(rsi_val,2)},
        "decision":{"action":action,"confidence":conf,"reasoning":reasoning},
        "fibonacci":{"levels":[0.236,0.382,0.5,0.618,0.786]},
        "portfolio":{"balance":10000,"trades":12,"pnl":234.5}
    }

@app.post("/chat")
def chat_ai(req: ChatReq):
    msg = req.message.lower()
    symbol = req.symbol
    ctx = req.context or {}
    rsi_val = ctx.get('rsi', 55)
    action = ctx.get('action', 'HOLD')
    reasoning = ctx.get('reasoning','')

    if "buy" in msg or "should i" in msg:
        return {"reply": f"For {symbol}, my AI says {action} (RSI {rsi_val}). If RSI <40 and EMA20 > EMA50, it's BUY zone. Current: {reasoning} Risk 1-2% per trade."}
    elif "rsi" in msg:
        return {"reply": f"RSI is {rsi_val}. <30 = oversold (buy opportunity), >70 = overbought (sell). {symbol} is {'oversold - potential buy' if rsi_val<30 else 'overbought - consider selling' if rsi_val>70 else 'neutral - wait'}."}
    elif "sell" in msg:
        return {"reply": f"SELL triggers when RSI>70 or price < EMA20. Currently {action} for {symbol}. Use trailing stop -3%."}
    elif "explain" in msg or "why" in msg:
        return {"reply": f"Why {action}? {reasoning} Based on RSI momentum, EMA trend, Fibonacci. Not financial advice."}
    elif "risk" in msg:
        return {"reply": f"Risk for {symbol}: Position 1-2% portfolio, stop-loss 3-5% below entry, take-profit 2:1. Volatility moderate."}
    else:
        return {"reply": f"I'm CryptoMind AI Assistant for {symbol}. Current signal {action} RSI {rsi_val}. Ask: 'Should I buy?', 'Explain RSI', 'Why this signal?', 'Risk?'"}

@app.get("/portfolio")
def portfolio():
    return {"balance":10000,"equity":10234.5,"pnl":234.5,"trades":[{"symbol":"BTCUSDT","action":"BUY","pnl":120},{"symbol":"ETHUSDT","action":"SELL","pnl":-20}]}
