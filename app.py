from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据库
data_store = {}

# 添加数据的 API
@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    if not data or 'name' not in data or 'type' not in data:
        return jsonify({'error': 'Missing name or type in request'}), 400

    # 存储数据，使用名称作为键
    data_store[data['name']] = data
    return jsonify({'message': 'Data added', 'data': data}), 201

# 获取数据的 API
@app.route('/api/data/<name>', methods=['GET'])
def get_data(name):
    if name in data_store:
        return jsonify(data_store[name])
    else:
        return jsonify({'error': 'Data not found'}), 404

# 删除数据的 API
@app.route('/api/data/<name>', methods=['DELETE'])
def delete_data(name):
    if name in data_store:
        del data_store[name]
        return jsonify({'message': 'Data deleted'})
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
