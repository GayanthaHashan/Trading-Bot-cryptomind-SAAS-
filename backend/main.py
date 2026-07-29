
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()

# Import core
from core.data_fetcher import fetch_klines
from core.technical_engine import analyze_technicals
from core.fibonacci import get_fib_levels
from core.news_sentiment import get_news_sentiment
from core.ai_brain import make_decision
from core.executor import PaperExecutor

app = FastAPI(title="CryptoMind AI")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Req(BaseModel):
    symbol: str = "BTCUSDT"
    interval: str = "1h"
    paper_trade: bool = True

executor = PaperExecutor()

@app.get("/")
def root():
    return {"status":"CryptoMind AI online", "mode":"low-compute", "docs":"/docs"}

@app.post("/analyze")
def analyze(req: Req):
    df = fetch_klines(req.symbol, req.interval, limit=200)
    tech = analyze_technicals(df)
    fib = get_fib_levels(df)
    news = get_news_sentiment(req.symbol)
    decision = make_decision(df, tech, fib, news)
    trade = None
    if req.paper_trade and decision['confidence'] >= 0.70:
        trade = executor.execute(decision)
    return {"symbol": req.symbol, "technical": tech, "fibonacci": fib, "news": news, "decision": decision, "portfolio": executor.get_status(), "trade": trade}

@app.get("/portfolio")
def portfolio():
    return executor.get_status()
