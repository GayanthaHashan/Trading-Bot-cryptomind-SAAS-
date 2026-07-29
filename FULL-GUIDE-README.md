
# CRYPTOMIND AI - FULL SETUP GUIDE
# From Zero to Cloud SaaS (0% PC Storage)

## PART 0: WHAT YOU WILL BUILD
You asked: "my drives going to full or not?"
Answer: 
- Local version: 180MB only (1 small movie), auto-deletes candles after use
- Cloud SaaS version: 0MB on your PC. You just open https://your-app.vercel.app

We will build CLOUD version. Your PC is only a remote control.

=================================================================
PART 1: GET FREE TESTNET KEYS (2 MIN) - NO REAL MONEY RISK
=================================================================
1. Open https://testnet.binance.vision/
2. Click "Log In" -> Login with GitHub account (create GitHub if needed)
3. Scroll down -> "Generate HMAC_SHA256 Key" -> Copy API Key and Secret
4. Save them in Notepad. These are FAKE money, you can practice.

=================================================================
PART 2: PREPARE CODE ON YOUR PC (3 MIN)
=================================================================
You already have code. Steps:

1. Download: CryptoMind-Setup.zip from chat
2. Extract to C:\CryptoMind\ (or /Users/yourname/CryptoMind on Mac)
3. Inside you see:
   C:\CryptoMind\backend\  <- Brain
   C:\CryptoMind\frontend\ <- Dashboard

Check backend has: main.py, core/, requirements.txt

=================================================================
PART 3: HOST BRAIN IN CLOUD - RENDER.COM (5 MIN)
=================================================================
This puts the AI brain in USA cloud server. Your PC can be OFF and it still trades.

1. Go to https://github.com -> Create account -> New Repository -> Name: cryptomind-saas -> Create
   - Click "Add file" -> "Upload files" -> Drag entire backend folder -> Commit

2. Go to https://render.com -> Sign up with GitHub -> Dashboard -> New + -> Web Service
   - Connect repository cryptomind-saas
   - Name: cryptomind-backend
   - Runtime: Python 3
   - Build Command: pip install -r backend/requirements.txt  (or pip install -r requirements.txt if you uploaded backend files directly to root)
   - Start Command: uvicorn main:app --host 0.0.0.0 --port 10000 --app-dir backend
     If you uploaded backend files to root, use: uvicorn main:app --host 0.0.0.0 --port 10000
   - Plan: Free

3. Scroll to Environment -> Add variables:
   BINANCE_API_KEY = your_testnet_key
   BINANCE_API_SECRET = your_testnet_secret
   USE_TESTNET = True

4. Click Create Web Service -> Wait 3 min -> You get URL like:
   https://cryptomind-backend-xyz.onrender.com
   Open it -> should show {"status":"CryptoMind AI online"}

   Copy this URL. This is your CLOUD BRAIN.

=================================================================
PART 4: HOST DASHBOARD IN CLOUD - VERCEL.COM (3 MIN)
=================================================================
This gives you the link you open to trade, like app.cryptomind.ai

1. Go to https://vercel.com -> Sign up with GitHub
2. Add New -> Project -> Import cryptomind-saas repo
3. Framework Preset: Other
4. Deploy -> Wait 1 min -> You get https://cryptomind-saas.vercel.app

   Open it on phone too! Add to Home Screen -> Share -> Add to Home Screen.

=================================================================
PART 5: CONNECT FRONTEND TO BACKEND
=================================================================
In Vercel project -> Settings -> Environment Variables -> Add:
   VITE_API_URL = https://cryptomind-backend-xyz.onrender.com  (your Render URL)

Redeploy in Vercel.

Now your dashboard calls cloud brain, not your PC.

=================================================================
PART 6: USE IT - NO PC STORAGE
=================================================================
1. Open https://cryptomind-saas.vercel.app
2. Login (demo login for now)
3. Select BTC/USDT -> Click Analyze -> You see AI analysis from cloud
4. Click Execute Paper Trade -> It runs on Render cloud, not your PC
5. Check portfolio: https://cryptomind-backend-xyz.onrender.com/portfolio
6. Turn Auto-Trade ON: In Render -> Your service -> Add Cron Job or use auto.py:
   In backend, create file auto_trader.py:
   
   import time, requests, os
   API = os.getenv("RENDER_URL", "http://localhost:8000")
   while True:
       try:
           r = requests.post(f"{API}/analyze", json={"symbol":"BTCUSDT","interval":"1h","paper_trade":True}, timeout=30)
           print(r.json()['decision'])
       except Exception as e:
           print(e)
       time.sleep(900)  # 15 min

   On Render, add this as Background Worker service.

Your PC storage used: 0 MB. Everything is in cloud.

=================================================================
PART 7: LOCAL RUN (OPTIONAL, IF YOU WANT TO TEST BEFORE CLOUD)
=================================================================
If you want to test on PC first (still only 180MB):

Windows PowerShell:
cd C:\CryptoMind\backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
notepad .env  (paste keys)
uvicorn main:app --reload --port 8000

Open http://localhost:8000/docs -> Try /analyze

Second terminal for frontend:
cd C:\CryptoMind\frontend
npm install
npm run dev
Open http://localhost:5173

=================================================================
PART 8: GO REAL MONEY (AFTER 1 MONTH PAPER TRADING)
=================================================================
WARNING: Only after you test 1 month on testnet.

1. Real Binance -> Profile -> API Management -> Create API
2. Enable ONLY "Enable Trading", DISABLE Withdrawal
3. Set IP whitelist: put your Render outbound IP (find in Render dashboard -> Connect -> Outbound IPs)
4. In Render -> Environment -> Change:
   BINANCE_API_KEY = real key
   BINANCE_API_SECRET = real secret
   USE_TESTNET = False
5. Start with $20-50, max 10% per trade, 2% stop loss hard-coded.

=================================================================
STORAGE EXPLANATION
=================================================================
Q: Will my C: drive get full?
A: No.
- Cloud SaaS: 0MB. All data in Render (1GB free) and Neon Postgres (0.5GB free)
- Local: backend = 30MB code + 150MB Python libs = 180MB total
- We never save 1-minute candles forever. We fetch 200 candles (50KB), analyze, delete. Not storing years of data.
- Trade history: 1 trade = 0.5KB. 10,000 trades = 5MB.

Q: Can I run from phone?
A: Yes, after cloud deploy, open Vercel link on phone.

Q: What if my PC shuts down?
A: Cloud version keeps running on Render. You get Telegram alerts (add Telegram bot later).

=================================================================
TROUBLESHOOTING
=================================================================
- Render says "Failed to build": Check Build Command is pip install -r backend/requirements.txt
- Vercel shows blank: Check VITE_API_URL env var is set to Render URL
- Binance error -1021: Time sync issue, Render fixes auto
- No data: You used real keys with USE_TESTNET=True -> set correctly

=================================================================
FILES INCLUDED IN THIS ZIP
=================================================================
- backend/main.py - FastAPI brain
- backend/core/* - data fetcher, technicals, fib, news, ai_brain, executor
- Dockerfile - for cloud deploy
- render.yaml - 1-click deploy config
- DEPLOY_GUIDE.md - this file

Need help? Tell me which step you stuck on.
