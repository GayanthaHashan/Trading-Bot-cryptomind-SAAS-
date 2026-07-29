
def make_decision(df, tech, fib, news):
    score=0; reasons=[]
    if 45 < tech['rsi'] < 70: score+=1; reasons.append(f"RSI {tech['rsi']} healthy")
    if tech['macd_signal']=="bullish": score+=1; reasons.append("MACD bullish crossover")
    if tech['close'] > tech['ema20'] > tech['ema50']: score+=1; reasons.append("Price > EMA20 > EMA50 uptrend")
    bullish=[p for p in tech['patterns'] if p['type']=='bullish']
    score+=len(bullish)*0.8
    if bullish: reasons.append(f"Detected {', '.join([p['name'] for p in bullish])}")
    if fib['nearest_fib']['distance_pct']<0.8 and float(fib['nearest_fib']['ratio']) in [0.5,0.618]:
        score+=1.2; reasons.append(f"Near Fib {fib['nearest_fib']['ratio']} support")
    if news['overall_score']>0.65: score+=1; reasons.append(f"News {news['overall_label']} {news['overall_score']}")
    max_score=6; confidence=min(score/max_score,0.95)
    if confidence>=0.70:
        action="BUY"; entry=tech['close']; sl=entry*0.98; tp=entry*1.04
    elif confidence<=0.35 and news['overall_score']<0.4:
        action="SELL"; entry=tech['close']; sl=entry*1.02; tp=entry*0.96
    else:
        action="HOLD"; entry=tech['close']; sl=tp=None
    return {"action":action,"confidence":round(confidence,2),"entry":entry,"stop_loss":sl,"take_profit":tp,"risk_reward":"1:2" if action!="HOLD" else None,"reasoning":" | ".join(reasons)[:300],"raw_score":score}
