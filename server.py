from flask import Flask, request, jsonify

app = Flask(__name__)
todoListsList = {}


@app.route('/todo-list', methods=['POST'])
def PostTodoList():
        todoListsList['todo_list'] = request.args

@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE'])
def GetTodoList(list_id):

@app.route('/todo-list/<list_id>/entry', methods=['POST'])

@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT', 'DELETE'])

@app.route('/user', methods=['GET', 'POST'])

@app.route('/user/<user_id>', methods=['DELETE'])

