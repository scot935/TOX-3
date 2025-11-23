from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'UUU-3-B2026_CARD_COUSTMER88654_AUTH'

# Dummy user (kept just in case you want it later)
USER = {'username': 'UUU3', 'password': 'Michael00000'}

def sanitize_input(value: str) -> str:
    return value.strip()

def is_valid_text(value: str) -> bool:
    return bool(re.match(r"^[A-Za-z0-9@._-]{1,40}$", value))

@app.route('/')
def home():
    return redirect(url_for('dashboard'))  # directly go to dashboard

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login page still exists but immediately redirects to dashboard
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    # REMOVED THE LOGIN CHECK → everyone can see the dashboard
    return render_template('dashboard.html', user="Guest")  # or any name you want

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))