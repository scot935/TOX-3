from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'UUU-3-B2026_CARD_COUSTMER88654_AUTH'

# Your real credentials
USERNAME = 'UUU3'
PASSWORD = 'Michael00000'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd  = request.form.get('password')

        # ←←← ONLY THIS PART IS ADDED BACK bro ←←←
        if user == USERNAME and pwd == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return "Wrong username or password bro! Go away."

    return render_template('login.html')  # you already have this file

@app.route('/dashboard')
def dashboard():
    # Simple check - if not logged in → kick back to login
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user=USERNAME)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))