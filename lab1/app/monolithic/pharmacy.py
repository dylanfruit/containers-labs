from flask import Flask, request, jsonify, json

app = Flask(__name__)

# Dummy data structures to represent inventory, customers, and orders
inventory = {
    'medicine_A': {'stock': 99, 'price': 10},
    'medicine_B': {'stock': 49, 'price': 15},
    # ... other medicines
}

customers = {
    'customer_id_1': {'name': 'John Doe', 'address': '123 Main St'},
    'customer_id_2': {'name': 'Alice Smith', 'address': '456 Elm St'},
    # ... other customers
}

orders = []

@app.route('/')
def index():
    return "Pharmacy v1"

@app.route('/place_order', methods=['POST'])
def place_order():
    order_details = request.json
    
    # Check if the requested medicine is available in inventory
    medicine_name = order_details['medicine']
    if medicine_name not in inventory:
        return json.dumps({'mesage': 'Medicine not available'}, indent=4)
        #return jsonify({'message': 'Medicine not available'})
    
    requested_quantity = order_details['quantity']
    available_quantity = inventory[medicine_name]['stock']
    
    if requested_quantity > available_quantity:
        return json.dumps({'message': 'Insufficient stock'}, indent=4)
        #return jsonify({'message': 'Insufficient stock'})
    
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
    
    return json.dumps({'message': 'Order placed successfully'}, indent=4)
    #return jsonify({'message': 'Order placed successfully', 'order_details': order})


@app.route('/view_inventory', methods=['GET'])
def view_inventory():
    return json.dumps({'inventory': inventory}, indent=4)
    #return jsonify({'inventory': inventory})


@app.route('/view_orders', methods=['GET'])
def view_orders():
    return json.dumps({'orders': orders}, indent=4)
    #return jsonify({'orders': orders})


@app.route('/view_customer/<customer_id>', methods=['GET'])
def view_customer(customer_id):
    if customer_id not in customers:
        return json.dumps({'message': 'Customer not found'}, indent=4)
        #return jsonify({'message': 'Customer not found'})
    
    return json.dumps({'customer_details': customers[customer_id]}, indent=4)
    #return jsonify({'customer_details': customers[customer_id]})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
