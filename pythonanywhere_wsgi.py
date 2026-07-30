
# PythonAnywhere WSGI file - Copy this to Web tab -> WSGI configuration file
import sys
import os

# TODO: Replace yourusername with your PythonAnywhere username
# Example: if username is cryptomindlk, path is /home/cryptomindlk/backend
USERNAME = 'yourusername'  # CHANGE THIS

path = f'/home/{USERNAME}/backend'
if path not in sys.path:
    sys.path.append(path)

path2 = f'/home/{USERNAME}'
if path2 not in sys.path:
    sys.path.append(path2)

# Import FastAPI app
from main import app as application
