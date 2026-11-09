from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/orders")
def orders():
    return jsonify([
        {"order_id": 101, "product_id": 1, "qty": 1},
        {"order_id": 102, "product_id": 2, "qty": 3},
    ])


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
