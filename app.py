import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort
import random

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_news(index):
    conn = get_db_connection()
    news = conn.execute('SELECT * FROM news WHERE "index" = ?',
                        (index,)).fetchone()
    conn.close()
    if news is None:
        abort(404)
    return news

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    news = conn.execute('SELECT * FROM news ORDER BY RANDOM() LIMIT 1;').fetchall()
    conn.close()
    return render_template('index.html', news=news)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=5000)