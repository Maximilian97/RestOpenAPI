import uuid

from flask import Flask, request, jsonify, abort

app = Flask(__name__)

userId1 = uuid.uuid4
userId2 = uuid.uuid4
userId3 = uuid.uuid4

todoListId1 = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todoListId2 = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todoListId3 = '44b02e00-03bc-451d-8d01-0c67ea866fee'

todoId1 = uuid.uuid4
todoId2 = uuid.uuid4
todoId3 = uuid.uuid4
todoId4 = uuid.uuid4

userList = [
        {'id': userId1, 'name': 'Konpachiro'},
        {'id': userId2, 'name': 'Kirk'},
        {'id': userId3, 'name': 'Johnny'}
]

todoLists = [
        {'id': todoListId1, 'name': 'Tagesziele'},
        {'id': todoListId2, 'name': 'Neue Liste 1'},
        {'id': todoListId3, 'name': 'Arbeit'}
]

todos = [
        {'id': todoId1, 'name': 'Fische füttern', 'description': '', 'list': todoListId2, 'user': userId1},
        {'id': todoId2, 'name': 'Emails schreiben', 'description': '', 'list': todoListId3, 'user': userId3},
        {'id': todoId3, 'name': 'Laufen gehen', 'description': '', 'list': todoListId1, 'user': userId1},
        {'id': todoId4, 'name': 'Müll rausbringen', 'description': '', 'list': todoListId1, 'user': userId2}
]

@app.route('/todo-list', methods=['POST'])
def PostTodoList():
        newList = request.get_json
        print('The list {} will be added'.format(newList))
        newList['id'] = uuid.uuid4
        todoLists.append(newList)
        return jsonify(newList), 200

@app.route('/todo-list/<list_id>', methods=['GET', 'DELETE'])
def HandleTodoList(list_id):
        requestType = request.method
        listItem = None

        for l in todoLists:
                if l['id'] == list_id:
                        listItem = l
                        break     
        match requestType:
                case 'GET':
                        print('Returning todo list...')
                        return jsonify([i for i in todos if i['list'] == list_id])
                case 'DELETE':
                        print('Deleting todo list...')
                        todoLists.remove(listItem)
                        return '', 200
                case _:
                        abort(404)

@app.route('/todo-list/<list_id>/entry', methods=['POST'])
def PostTodoListEntry(list_Id):
        newTodo = request.get_json
        listItem = None

        for l in todoLists:
                if l['id'] == list_Id:
                        listItem = l
                        break
        newTodo['id'] = uuid.uuid4


@app.route('/todo-list/<list_id>/entry/<entry_id>', methods=['PUT', 'DELETE'])

@app.route('/user', methods=['GET', 'POST'])
def HandleUser():
        requestType = request.method

        match requestType:
                case 'GET':
                        return jsonify([i for i in userList])
                case 'POST':
                        newUser = request.get_json
                        newUser[id] = uuid.uuid4
                        userList.append(newUser)
                        return '', 200
                case _:
                        abort(404)

                        

@app.route('/user/<user_id>', methods=['DELETE'])
def DeleteUser(user_id):
        for l in userList:
                if l['id'] == user_id:
                        listItem = l
                        break

        userList.remove(listItem)
        return '', 200


