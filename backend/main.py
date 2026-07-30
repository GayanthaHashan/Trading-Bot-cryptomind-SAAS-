
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="CryptoMind AI - Works 100% No Card")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

try:
    from core.data_fetcher import fetch_klines
    from core.technical_engine import analyze_technicals
    from core.fibonacci import get_fib_levels
    from core.news_sentiment import get_news_sentiment
    from core.ai_brain import make_decision
    from core.executor import PaperExecutor
    HAS_CORE=True
    executor = PaperExecutor()
except Exception as e:
    HAS_CORE=False
    IMPORT_ERROR=str(e)

@app.get("/")
def root():
    if HAS_CORE:
        return {"status":"Cloud SaaS Online - Works 100% No Card","platform":"PythonAnywhere/Replit/Vercel","pc_storage":"0MB","ram":"512MB-1GB free","no_card":True}
    else:
        return {"status":"Core missing","error":IMPORT_ERROR,"fix":"Upload core folder"}

from pydantic import BaseModel
class Req(BaseModel):
    symbol: str = "BTCUSDT"
    interval: str = "1h"
    paper_trade: bool = True

@app.post("/analyze")
def analyze(req: Req):
    if not HAS_CORE:
        return {"error":"Core files missing"}
    try:
        df = fetch_klines(req.symbol, req.interval, 200)
        tech = analyze_technicals(df)
        fib = get_fib_levels(df)
        news = get_news_sentiment(req.symbol)
        decision = make_decision(df, tech, fib, news, None)
        trade = executor.execute(decision) if req.paper_trade and decision['confidence']>=0.70 else None
        return {"symbol":req.symbol,"technical":tech,"fibonacci":fib,"news":news,"decision":decision,"portfolio":executor.get_status(),"trade":trade}
    except Exception as e:
        return {"error":str(e)}

@app.get("/portfolio")
def portfolio():
    if not HAS_CORE:
        return {"error":"Core missing"}
    return executor.get_status()

@app.get("/health")
def health():
    return {"ok":True}
