"""service for orders"""
from flask import Flask, json, request
import json
import os

app = Flask(__name__)

# File to store orders
ORDERS_FILE = '/data/orders.json'

# Create the orders file if it doesn't exist
if not os.path.exists(ORDERS_FILE):
   with open(ORDERS_FILE, 'w') as f:
      json.dump([], f)

def read_orders():
   """Read orders from file"""
   with open(ORDERS_FILE, 'r') as f:
      return json.load(f)

def write_orders(orders):
   """Write orders to file"""
   with open(ORDERS_FILE, 'w') as f:
      json.dump(orders, f, indent=2)

# Endpoint to place orders
@app.route('/place_order', methods=['POST'])
def place_order():
    """Receives orders"""
    order_details = request.json
    medicine_name = order_details['medicine']
    requested_quantity = order_details['quantity']

    # Prepare order details
    order = {
        'customer_id': order_details['customer_id'],
        'medicine': medicine_name,
        'quantity': requested_quantity,
        'status': 'Pending'
    }
    
    allorders = read_orders()
    allorders.append(order)
    write_orders(allorders)

    return json.dumps({'message': 'Order placed successfully'}, indent=4)

# Endpoint to view orders
@app.route('/view_orders', methods=['GET'])
def view_orders():
    """Print existing orders"""
    allorders = read_orders()
    return json.dumps({'orders': allorders}, indent=4)

if __name__ == '__main__':
    app.run(port=5002)
