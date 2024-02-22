from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    origin_city = request.args.get('originCity')
    destination_city = request.args.get('destinationCity')
    airline = request.args.get('airline')
    conn = get_db_connection()
    flights = conn.execute(f"SELECT * FROM flights where origin_city='{origin_city}' and destination_city='{destination_city}'").fetchall()
    conn.close()
    return render_template('search.html', flights=flights)

