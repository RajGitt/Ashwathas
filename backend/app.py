from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
DB = 'products.db'

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            image TEXT,
            sizes TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Ashwathas backend is running!"

@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect(DB)
    cursor = conn.execute('SELECT * FROM products')
    products = [
        {"id": row[0], "name": row[1], "image": row[2], "sizes": row[3].split(','), "price": row[4]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO products (name, image, sizes, price) VALUES (?, ?, ?, ?)", (
        data['name'], data['image'], ','.join(data['sizes']), data['price']
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=10000, debug=True)
