import os
from flask import Flask, request, jsonify
from src.handlers.transaction_handler import handle_transaction

app = Flask(__name__)

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    transaction = handle_transaction(data)
    return jsonify(transaction.__dict__), 201

if __name__ == '__main__':
    app.run()