from flask import Flask, jsonify

app = Flask(__name__)

customers = {
    'customer_id_1': {'name': 'John Doe', 'address': '123 Main St'},
    'customer_id_2': {'name': 'Alice Smith', 'address': '456 Elm St'},
    # ... other customers
}

@app.route('/view_customer/<customer_id>', methods=['GET'])
def view_customer(customer_id):
    if customer_id not in customers:
        return jsonify({'message': 'Customer not found'}), 404
    
    return jsonify({'customer_details': customers[customer_id]}), 200

if __name__ == '__main__':
    app.run(port=5003)