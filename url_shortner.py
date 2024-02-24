from flask import Flask, request, redirect, render_template_string
import sqlite3
import string
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def get_connection():
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    return conn

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(6))
    return short_url

@app.route('/')
def index():
    return render_template_string('''
        <h1>URL Shortener</h1>
        <form method="POST" action="/shorten">
            <input type="text" name="url" placeholder="Enter URL here" required>
            <button type="submit">Shorten</button>
        </form>
    ''')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    short_url = generate_short_url()

    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    conn.commit()
    conn.close()

    return render_template_string('''
        <h1>URL Shortened</h1>
        <p>Your shortened URL is: <a href="{{ url_for('redirect_url', short_url=short_url) }}">{{ url_for('redirect_url', short_url=short_url) }}</a></p>
    ''', short_url=short_url)

@app.route('/<short_url>')
def redirect_url(short_url):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = c.fetchone()
    conn.close()

    if result:
        original_url = result['original_url']
        return redirect(original_url)
    else:
        return "Short URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
