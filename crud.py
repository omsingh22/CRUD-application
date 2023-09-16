from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory database)
data = {
    1: {"id": 1, "name": "Item 1"},
    2: {"id": 2, "name": "Item 2"},
}

# Create (POST) an item
@app.route('/items', methods=['POST'])
def create_item():
    req_data = request.get_json()
    if 'name' not in req_data:
        return jsonify({'message': 'Name is required'}), 400

    item_id = max(data.keys()) + 1
    item = {'id': item_id, 'name': req_data['name']}
    data[item_id] = item
    return jsonify({'message': 'Item created', 'item': item}), 201

# Read (GET) all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(list(data.values()))

# Read (GET) a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Update (PUT) an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = data.get(item_id)
    if not item:
        return jsonify({'message': 'Item not found'}), 404

    req_data = request.get_json()
    if 'name' in req_data:
        item['name'] = req_data['name']

    return jsonify({'message': 'Item updated', 'item': item})

# Delete (DELETE) an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = data.get(item_id)
    if item:
        del data[item_id]
        return jsonify({'message': 'Item deleted', 'item': item})
    return jsonify({'message': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
