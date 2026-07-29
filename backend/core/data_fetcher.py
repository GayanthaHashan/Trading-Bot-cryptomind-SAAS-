
import pandas as pd, os, random
from dotenv import load_dotenv
load_dotenv()

def fetch_klines(symbol="BTCUSDT", interval="1h", limit=200):
    # Try real Binance, fallback to mock if no keys or testnet
    try:
        from binance.client import Client
        key = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_API_SECRET")
        use_testnet = os.getenv("USE_TESTNET","True")=="True"
        if key and secret and "testnet" not in key and not use_testnet:
            client = Client(key, secret)
        elif key and secret:
            client = Client(key, secret, testnet=True)
            client.API_URL = 'https://testnet.binance.vision/api'
        else:
            raise Exception("No keys, use mock")
        klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
        df = pd.DataFrame(klines, columns=['ot','open','high','low','close','volume','ct','qav','trades','tb','tq','ig'])
        for c in ['open','high','low','close','volume']: df[c]=df[c].astype(float)
        return df
    except Exception as e:
        print(f"Using mock data because: {e}")
        # Generate realistic mock candles
        import numpy as np
        price = 67000 if "BTC" in symbol else 3500
        data=[]
        for i in range(limit):
            change = random.uniform(-0.008,0.008)
            open_p = price
            close_p = price*(1+change)
            high_p = max(open_p,close_p)*random.uniform(1,1.003)
            low_p = min(open_p,close_p)*random.uniform(0.997,1)
            data.append([0,open_p,high_p,low_p,close_p,random.uniform(10,100),0,0,0,0,0,0])
            price=close_p
        df=pd.DataFrame(data, columns=['ot','open','high','low','close','volume','ct','qav','trades','tb','tq','ig'])
        return df
