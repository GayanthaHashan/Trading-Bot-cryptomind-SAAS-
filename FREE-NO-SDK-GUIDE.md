
# 100% FREE - NO CARD - NO PAID SDK - MORE RAM
# For Sri Lanka - No Credit Card Needed

You said Hugging Face SDK needs paying. OK, we switch to 2 sites that are TOTALLY FREE with no SDK selection and more RAM:

=================================================================
BEST OPTION 1: KOYEB.COM - 512MB RAM FREE, NO CARD, NO SDK PAY
=================================================================
Koyeb is like Render but 100% free tier with NO CARD required. No SDK to choose. Just GitHub -> Deploy.

SPECS: 512MB RAM, 0.1 vCPU, 2GB disk, 100GB bandwidth - FREE, no card.

Steps (4 min):

1. Go to https://www.koyeb.com -> Sign up -> Continue with GitHub (no card)

2. Dashboard -> Create App -> Create Service -> Choose GitHub -> Select your repo cryptomind-saas
   If you didn't push to GitHub yet: Use "Deploy from GitHub" and upload ZIP method: Create App -> Upload Docker image? No, easier: Use GitHub.

   ALTERNATIVE NO GITHUB: Koyeb allows deploy from Docker Hub, but GitHub is easiest.

3. Settings page - FILL BEFORE DEPLOY:
   - Service name: cryptomind-backend
   - Builder: Dockerfile  (it auto detects your Dockerfile)
   - Port: 8000  (IMPORTANT - Koyeb needs 8000)
   - Instance: Free (0.1 vCPU, 512MB)

4. Environment Variables -> Add:
   BINANCE_API_KEY = your testnet key
   BINANCE_API_SECRET = your testnet secret
   USE_TESTNET = True
   PORT = 8000

5. Click Deploy -> Wait 2 min -> You get URL like:
   https://cryptomind-backend-xxx.koyeb.app

   Open it -> Should show {"status":"Cloud SaaS Online"}

Done! No card, no SDK pay, 512MB RAM free.

If you don't have GitHub, Koyeb also has "Deploy from Git" with public repo, still free.

=================================================================
BEST OPTION 2: PYTHONANYWHERE - EASIEST, NO SDK AT ALL, NO CARD
=================================================================
This site has NO SDK selection at all. Just upload Python files and click Reload. Made for beginners.

SPECS: 512MB RAM, 1 web app, 100% free, no card, no Docker needed.

Steps (3 min):

1. Go to https://www.pythonanywhere.com -> Create a Beginner Account (FREE, no card, only email)

2. After login, top menu -> Files -> Upload -> Upload ALL files from backend folder (main.py + core folder)

3. Go to Web tab -> Add a new web app -> 
   - Click Next -> Manual Configuration -> Python 3.10 -> Next -> Next

4. In Web tab, scroll to Code -> WSGI configuration file -> Click link to edit

   Delete everything and paste this:

import sys
path = '/home/yourusername/backend'
# Replace yourusername with your PythonAnywhere username shown at top
if path not in sys.path:
    sys.path.append(path)
path2 = '/home/yourusername'
if path2 not in sys.path:
    sys.path.append(path2)

from main import app as application

   Save.

5. Go back to Web tab -> Click green Reload button

6. Your URL is: https://yourusername.pythonanywhere.com
   Open https://yourusername.pythonanywhere.com/docs -> Test /analyze

No Docker, no SDK, no card, no Build Command. Just upload and Reload.

Pros: Easiest, no SDK pay, no card, perfect for you.

=================================================================
BEST OPTION 3: REPLIT - 1GB RAM FREE, NO CARD, NO SDK PAY, INSTANT
=================================================================
SPECS: 1GB RAM (more than Koyeb), 0.5 vCPU, FREE, no card.

1. https://replit.com -> Sign up free (no card)

2. + Create Repl -> Import from GitHub -> Paste your GitHub repo URL

3. Replit auto detects requirements.txt -> Click Run button (top)

4. It opens Webview with URL like https://cryptomind-backend.yourname.repl.co

5. Left sidebar -> Secrets (lock icon) -> Add:
   BINANCE_API_KEY, BINANCE_API_SECRET, USE_TESTNET=True

6. Click Run again

Done in 2 min. 1GB RAM free.

=================================================================
WHICH TO CHOOSE FOR MORE SPEC?
=================================================================
- More RAM: Replit = 1GB RAM free (most)
- Easiest no SDK: PythonAnywhere = no Docker, no SDK selection at all
- Closest to Render but no card: Koyeb = 512MB RAM, Docker free, no SDK pay

I recommend: PythonAnywhere for you (no SDK, no Docker, no card, very simple)

=================================================================
FRONTEND - STILL FREE NO CARD
=================================================================
Vercel.com -> Still free no card, no SDK pay.

Deploy frontend there -> Get https://your-app.vercel.app -> Open on phone.

Set env VITE_API_URL = your Koyeb/PythonAnywhere/Replit URL

Now: Phone (0MB) -> Vercel (free) -> Koyeb/PythonAnywhere (free, no card) -> Binance

0MB PC, $0/month, no card, no paid SDK.

=================================================================
DO YOU NEED TO UPGRADE FILES?
=================================================================
NO. Same files work on all 3 sites.

Only difference is port:
- Koyeb: 8000 (already set in our Dockerfile)
- PythonAnywhere: no port needed, they handle
- Replit: auto port

Our new ZIP already has correct files for all 3.

Just upload same backend folder to any of these 3 sites.

=================================================================
FINAL STEPS AFTER DEPLOY
=================================================================
1. Test backend: open https://your-url/docs -> Try POST /analyze -> Should return BUY/SELL
2. Deploy frontend to Vercel
3. Open frontend URL on phone -> Add to Home Screen
4. Trade from hosted system, 0MB PC

Tell me which of the 3 you want (Koyeb / PythonAnywhere / Replit) and I will give you exact 3 clicks for that one.
