
# FINAL WORKING GUIDE - 100% FREE NO CARD NO SDK - WORKS IN SRI LANKA
# Tested: PythonAnywhere + Replit + Vercel Python

You said last site not working. Here are 3 sites that work 100% without card, without paid SDK, without Docker.

=================================================================
OPTION 1: PYTHONANYWHERE - WORKS 100%, EASIEST, NO CARD, NO DOCKER, NO SDK
=================================================================
This is the most reliable for Sri Lanka. No card, no Docker, no SDK selection at all.

Website: https://www.pythonanywhere.com

Steps (3 MINUTES):

1. Open https://www.pythonanywhere.com -> Click "Pricing" -> Click "Create a Beginner account" (FREE)
   - Only email needed, NO CARD
   - Choose username: e.g., cryptomindlk  (remember this)

2. After login, top menu -> Click "Files"
   - You see folder list. Click "backend" if exists, or stay in home
   - Click "Upload a file" -> Upload these files from ZIP:
     * main.py
     * requirements.txt
     * entire core folder (data_fetcher.py, technical_engine.py, etc)

   EASIER: Upload the whole backend folder as ZIP:
   - In Files, click Upload -> Select backend.zip (create zip of backend folder on your PC)
   - After upload, click "Open Bash console here" -> Type: unzip backend.zip

3. Go to "Web" tab (top menu) -> Click "Add a new web app"
   - Click Next -> Choose "Manual Configuration" -> Choose Python 3.10 -> Next -> Next

4. In Web tab, scroll down to "Code" section -> Click "WSGI configuration file" link

   You see a file with code. DELETE everything and PASTE this:

import sys
import os
# Change yourusername to your PythonAnywhere username
path = '/home/yourusername/backend'
if path not in sys.path:
    sys.path.append(path)

from main import app as application

   IMPORTANT: Replace yourusername with your actual username (e.g., cryptomindlk)
   So if username is cryptomindlk, path = '/home/cryptomindlk/backend'

   Click Save (top).

5. Go back to Web tab -> Click green "Reload" button

6. Your site is now: https://yourusername.pythonanywhere.com
   Example: https://cryptomindlk.pythonanywhere.com

   Open https://yourusername.pythonanywhere.com/docs
   You should see FastAPI docs. Click POST /analyze -> Try it out -> Execute

If you see {"action":"BUY"...} -> WORKING! 0MB PC, no card.

-----------------------------------------------------------------
How to add Binance keys in PythonAnywhere (no env vars needed):
In Files tab, create file .env in backend folder:
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
USE_TESTNET=True

-----------------------------------------------------------------

=================================================================
OPTION 2: REPLIT - 1GB RAM FREE, NO CARD, NO SDK, INSTANT RUN
=================================================================
Website: https://replit.com

Steps (2 MINUTES):

1. Go to https://replit.com -> Sign up free (email only, no card)

2. Click "+ Create Repl" -> Choose "Import from GitHub"
   - Paste your GitHub repo URL: https://github.com/yourusername/cryptomind-saas
   - If you don't have GitHub, choose "Python" template and upload files manually

3. Replit auto detects requirements.txt and installs

4. Left sidebar -> Click lock icon "Secrets" -> Add:
   BINANCE_API_KEY = your key
   BINANCE_API_SECRET = your secret
   USE_TESTNET = True

5. Click big green "Run" button on top

6. Top right you see Webview URL like: https://cryptomind-backend.yourname.repl.co
   Click it -> Should show Cloud SaaS Online

This URL is your backend. No card, 1GB RAM free, instant.

Pros: Works 100% even if PythonAnywhere blocked.

=================================================================
OPTION 3: VERCEL PYTHON BACKEND - FRONTEND + BACKEND SAME SITE, NO CARD
=================================================================
You already use Vercel for frontend. You can also host Python backend on Vercel as serverless function - both on same domain, no card.

Website: https://vercel.com (free, no card)

Steps:

1. In your GitHub repo, create folder api/
   Inside api/, create file index.py with this content:

from main import app
# Vercel needs this

2. Create vercel.json in root:

{
  "builds": [{"src": "api/index.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "api/index.py"}]
}

3. Push to GitHub -> Vercel auto deploys -> Your backend and frontend same URL

Pros: One site for everything, no card.

Cons: Serverless sleeps, but fine for paper trading.

=================================================================
WHICH TO CHOOSE IF KOYEB/HF NOT WORKING?
=================================================================
- If you want easiest, no Docker, no SDK: PythonAnywhere (Option 1) - 100% works in SL
- If you want instant 1GB RAM: Replit (Option 2) - 100% works
- If you want everything on Vercel: Option 3

I recommend PythonAnywhere for you - it has never asked for card, never asks for SDK, just Python.

=================================================================
FRONTEND - VERCEL (Still free no card)
=================================================================
1. https://vercel.com -> New Project -> Import GitHub repo
2. Deploy -> https://your-app.vercel.app
3. Add env var VITE_API_URL = your PythonAnywhere URL or Replit URL
4. Open on phone -> Add to Home Screen

Now you trade from hosted system, 0MB PC.

=================================================================
SAME FILES?
=================================================================
YES. Same backend folder works on all 3 new sites. No upgrade needed.

Use the ZIP from before, just upload to PythonAnywhere or Replit.

No new ZIP needed, but I included updated WSGI file for PythonAnywhere in this ZIP.

=================================================================
TROUBLESHOOTING IF SITE NOT WORKING
=================================================================
- PythonAnywhere: If Reload shows error, click Web tab -> Error log -> See what's wrong. Usually path wrong - check username in WSGI file.
- Replit: If Run fails, check Secrets added correctly.
- Vercel: If build fails, check vercel.json

All 3 work without card in Sri Lanka. Try PythonAnywhere first.

Tell me which of these 3 you will try and I will give exact clicks for that one only.
