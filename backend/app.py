from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)
DB = 'products.db'

# ✅ Create database and table if not exists
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

# ✅ Root route to confirm app is running
@app.route('/')
def home():
    return "Ashwathas backend is running!"

# ✅ Fetch all products
@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect(DB)
    cursor = conn.execute('SELECT * FROM products')
    products = [
        {
            "id": row[0],
            "name": row[1],
            "image": row[2],
            "sizes": row[3].split(','),
            "price": row[4]
        }
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(products)

# ✅ Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO products (name, image, sizes, price) VALUES (?, ?, ?, ?)",
        (data['name'], data['image'], ','.join(data['sizes']), data['price'])
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

# ✅ Seed sample product
@app.route('/seed')
def seed():
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO products (name, image, sizes, price) VALUES (?, ?, ?, ?)",
        ("Ashwathas Tee", "https://via.placeholder.com/300", "S,M,L", 799)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Seeded product"})

# ✅ Run the app on the correct port
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
