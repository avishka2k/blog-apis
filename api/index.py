from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, API!"

@app.route("/products", methods=["GET"])
def products():
    products = [
        {"name": "Apples", "price": 2.99},
        {"name": "Bananas", "price": 1.99},
        {"name": "Carrots", "price": 0.99},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
