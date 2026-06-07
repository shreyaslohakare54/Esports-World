from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # For flashing messages

DB_PATH = 'esports.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    # Signin table
    c.execute('''
        CREATE TABLE IF NOT EXISTS signin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT
        )
    ''')
    # Solo registrations with slot and date
    c.execute('''
        CREATE TABLE IF NOT EXISTS solo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot TEXT,
            date TEXT,
            name TEXT,
            uid TEXT,
            mobile TEXT,
            age INTEGER,
            level INTEGER,
            email TEXT,
            screenshot BLOB
        )
    ''')
    # Squad registrations with slot and date
    c.execute('''
        CREATE TABLE IF NOT EXISTS squad (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            slot TEXT,
            date TEXT,
            name TEXT,
            uid TEXT,
            mobile TEXT,
            email TEXT,
            screenshot BLOB
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solo')
def solo():
    return render_template('solo.html')

@app.route('/squad')
def squad():
    return render_template('squad.html')

@app.route('/clash')
def clash():
    return render_template('clash.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    conn = get_db_connection()
    conn.execute('INSERT INTO signin (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()
    flash('Signed in successfully!')
    return redirect('/')

@app.route('/register-solo', methods=['POST'])
def register_solo():
    slot = request.form['slot']
    name = request.form['name']
    uid = request.form['uid']
    mobile = request.form['mobile']
    age = int(request.form['age'])
    level = int(request.form['level'])
    email = request.form['email']
    screenshot = request.files['screenshot'].read()

    today = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()

    # Check slot count limit 50 per day
    c = conn.execute('SELECT COUNT(*) FROM solo WHERE slot = ? AND date = ?', (slot, today))
    count = c.fetchone()[0]
    if count >= 50:
        flash(f"Sorry, the {slot} slot for Solo Tournament is full for today.")
        conn.close()
        return redirect('/solo')

    conn.execute('''
        INSERT INTO solo (slot, date, name, uid, mobile, age, level, email, screenshot)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (slot, today, name, uid, mobile, age, level, email, screenshot))
    conn.commit()
    conn.close()
    flash("Solo registration successful! Please wait for payment confirmation.")
    return redirect('/solo')

@app.route('/register-squad', methods=['POST'])
def register_squad():
    slot = request.form['slot']
    name = request.form['name']
    uid = request.form['uid']
    mobile = request.form['mobile']
    email = request.form['email']
    screenshot = request.files['screenshot'].read()

    today = datetime.now().strftime('%Y-%m-%d')
    conn = get_db_connection()

    if slot in ['6:00 PM', '9:00 PM']:
        c = conn.execute('SELECT COUNT(*) FROM squad WHERE slot = ? AND date = ?', (slot, today))
        count = c.fetchone()[0]
        if count >= 12:
            flash(f"Sorry, the {slot} slot for Squad Tournament is full for today.")
            conn.close()
            return redirect('/squad')

    conn.execute('''
        INSERT INTO squad (slot, date, name, uid, mobile, email, screenshot)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (slot, today, name, uid, mobile, email, screenshot))
    conn.commit()
    conn.close()
    flash("Squad registration successful! Please wait for payment confirmation.")
    return redirect('/squad')

if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        init_db()
    app.run(debug=True)
