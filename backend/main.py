
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CryptoMind AI - GitHub Codespace Works 100%")
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
    return {"status":"Cloud SaaS Online - GitHub Codespace - Works 100%","no_card":True,"no_sdk":True,"works_in_sri_lanka":True,"pc_storage":"0MB when using Codespace"}

from pydantic import BaseModel
class Req(BaseModel):
    symbol: str = "BTCUSDT"
    interval: str = "1h"
    paper_trade: bool = True

@app.post("/analyze")
def analyze(req: Req):
    if not HAS_CORE:
        return {"error":"Core missing","detail":IMPORT_ERROR}
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
    return executor.get_status() if HAS_CORE else {"error":"Core missing"}

@app.get("/health")
def health():
    return {"ok":True}
