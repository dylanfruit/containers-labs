from flask import Flask, jsonify

app = Flask(__name__)

inventory = {
    'medicine_A': {'stock': 100, 'price': 10},
    'medicine_B': {'stock': 50, 'price': 15},
    # ... other medicines
}

@app.route('/view_inventory', methods=['GET'])
def view_inventory():
    return jsonify({'inventory': inventory}), 200

if __name__ == '__main__':
    app.run(port=5001)
