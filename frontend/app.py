import os

import requests
from flask import Flask, jsonify

app = Flask(__name__)

PRODUCTS_URL = os.getenv("PRODUCTS_URL", "http://products-service:5001")
ORDERS_URL = os.getenv("ORDERS_URL", "http://orders-service:5002")


def fetch(url):
    try:
        return requests.get(url, timeout=3).json(), None
    except requests.RequestException as exc:
        return None, str(exc)


@app.route("/")
def home():
    products, p_err = fetch(f"{PRODUCTS_URL}/products")
    orders, o_err = fetch(f"{ORDERS_URL}/orders")
    errors = {k: v for k, v in (("products", p_err), ("orders", o_err)) if v}
    status = 502 if errors else 200
    return jsonify({"products": products, "orders": orders, "errors": errors}), status


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
