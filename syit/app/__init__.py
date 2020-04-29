from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.session_cookie_name = "your_session"
app.permanent_session_lifetime = 7200

from app import views