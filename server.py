from crypt import methods
import flask as Flask, request,jsonify

app = Flask(__name__) 

@app.route('/todo-list', methods=['POST'])
def postTodoList():
        return jsonify(request.args)

@app.route('/todo-list', methods=['GET'])
def postTodoList():
        return jsonify(request.args)
        

