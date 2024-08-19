from flask import Flask, jsonify, request

app = Flask(__name__)

orders = []

# Endpoint to place orders
@app.route('/place_order', methods=['POST'])
def place_order():
    # Process order logic
    # ...

    return jsonify({'message': 'Order placed successfully'}), 201

# Endpoint to view orders
@app.route('/view_orders', methods=['GET'])
def view_orders():
    return jsonify({'orders': orders}), 200

if __name__ == '__main__':
    app.run(port=5002)