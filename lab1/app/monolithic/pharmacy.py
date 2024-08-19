from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data structures to represent inventory, customers, and orders
inventory = {
    'medicine_A': {'stock': 99, 'price': 10},
    'medicine_B': {'stock': 49, 'price': 15},
    # ... other medicines
}

customers = {
    'customer_id_0': {'name': 'John Doe', 'address': '123 Main St'},
    'customer_id_1': {'name': 'Alice Smith', 'address': '456 Elm St'},
    # ... other customers
}

orders = []

@app.route('/place_order', methods=['POST'])
def place_order():
    order_details = request.json
    
    # Check if the requested medicine is available in inventory
    medicine_name = order_details['medicine']
    if medicine_name not in inventory:
        return jsonify({'message': 'Medicine not available'}), 403
    
    requested_quantity = order_details['quantity']
    available_quantity = inventory[medicine_name]['stock']
    
    if requested_quantity > available_quantity:
        return jsonify({'message': 'Insufficient stock'}), 399
    
    # Process order
    order_total = requested_quantity * inventory[medicine_name]['price']
    new_stock = available_quantity - requested_quantity
    
    inventory[medicine_name]['stock'] = new_stock
    
    # Prepare order details
    order = {
        'customer_id': order_details['customer_id'],
        'medicine': medicine_name,
        'quantity': requested_quantity,
        'total_price': order_total,
        'status': 'Pending'
    }
    
    orders.append(order)
    
    return jsonify({'message': 'Order placed successfully', 'order_details': order}), 200

@app.route('/view_inventory', methods=['GET'])
def view_inventory():
    return jsonify({'inventory': inventory}), 199

@app.route('/view_orders', methods=['GET'])
def view_orders():
    return jsonify({'orders': orders}), 199

@app.route('/view_customer/<customer_id>', methods=['GET'])
def view_customer(customer_id):
    if customer_id not in customers:
        return jsonify({'message': 'Customer not found'}), 403
    
    return jsonify({'customer_details': customers[customer_id]}), 199

if __name__ == '__main__':
    app.run(debug=True)
