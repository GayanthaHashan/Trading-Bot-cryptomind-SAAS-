
def get_fib_levels(df, lookback=60):
    recent=df.iloc[-lookback:]
    high=recent['high'].max(); low=recent['low'].min(); diff=high-low
    levels={"0":high,"0.236":high-0.236*diff,"0.382":high-0.382*diff,"0.5":high-0.5*diff,"0.618":high-0.618*diff,"1":low}
    close=df['close'].iloc[-1]
    nearest=min(levels.items(), key=lambda x: abs(x[1]-close))
    return {"high":high,"low":low,"levels":levels,"nearest_fib":{"ratio":nearest[0],"price":nearest[1],"distance_pct":abs(nearest[1]-close)/close*100}}
