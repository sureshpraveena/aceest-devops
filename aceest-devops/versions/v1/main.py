from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = 'clients.db'
# client = []  # List to store client data

# DB Initialization
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            age INTEGERL,
            weight REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "ACEest v1.0 is running!"

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.get_json()
    # Process the client data (e.g., save to database)
    conn = sqlite3.connect(DB_NAME)
    cur  = conn.cursor()

    cur.execute('''
        INSERT INTO clients (name, email, age, weight) VALUES (?, ?, ?, ?)
    ''', (data['name'], data.get('email'), data.get('age'), data.get('weight')))
    conn.commit()
    conn.close()

    # client.append(data)  # Assuming 'client' is a list to store client data
    return jsonify({"message": "Client created successfully"}), 200

@app.route("/clients", methods=["GET"])
def get_clients():
    # Retrieve client data (e.g., from database)
    conn = sqlite3.connect(DB_NAME)
    cur  = conn.cursor()
    cur.execute('SELECT * FROM clients')
    rows = cur.fetchall()
    clients = []
    for row in rows:
        clients.append({
            "id"    : row[0],
            "name"  : row[1],
            "email" : row[2],
            "age"   : row[3],
            "weight": row[4]
        })
    return jsonify(clients), 200

if __name__ == "__main__":
    init_db()
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)