from os import abort
from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    print(todos, 'todo')
    json_text = jsonify(todos)
    print(json_text, 'json')
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_data = request.get_json(force=True)
    new_todo = {
       
        'label': request_data.get('label', ''),
        'done': request_data.get('done', False)
    }
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        abort(404)
    deleted_item = todos.pop(position)
    return jsonify(todos)



    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)