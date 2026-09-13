import os
from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 799},
    {"id": 2, "name": "Mouse", "price": 15},
]


@app.route("/products")
def get_products():
    return jsonify({
        "service": "products-service",
        "version": os.environ.get("APP_VERSION", "v1"),
        "products": products
    })


@app.route("/products/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
