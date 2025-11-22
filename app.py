from flask import Flask, render_template, request, redirect, url_for, session
from flask_cors import CORS
import os
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.secret_key = 'UUU-3-B2026_CARD_COUSTMER88654_AUTH'

# Dummy user
USER = { 'username': 'UUU3', 'password': 'Michael00000' }

def sanitize_input(value: str) -> str:
    """Trim and ensure it's a clean string."""
    return value.strip()

def is_valid_text(value: str) -> bool:
    """Basic security: avoid weird characters."""
    return bool(re.match(r"^[A-Za-z0-9@._-]{1,40}$", value))


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = sanitize_input(request.form.get('username', ''))
        pword = sanitize_input(request.form.get('password', ''))

        # --- Validation ---
        if not uname or not pword:
            return render_template('login.html', error="Fields cannot be empty")

        if len(uname) < 3 or len(pword) < 5:
            return render_template('login.html', error="Invalid username or password length")

        if not is_valid_text(uname) or not is_valid_text(pword):
            return render_template('login.html', error="Invalid characters entered")

        # --- Authentication ---
        if uname == USER['username'] and pword == USER['password']:
            session['user'] = uname
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
