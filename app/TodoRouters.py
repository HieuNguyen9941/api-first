from flask import Blueprint, request, json
from .Todo import get_all_todo, add_todo_controller, update_todo_controller, delete_todo_controller,get_todo_by_id_controler


todo = Blueprint('todo', __name__)

# http://localhost:5000/api/todo  method = GET
@todo.route('/api/todo', methods=['GET'])
def get_all():
    return json.htmlsafe_dumps(get_all_todo()) 

# http://localhost:5000/api/todo/?id=3 method = GET
@todo.route('/api/todo/', methods=['GET'])
def get_todo():
    id = request.args['id']
    return json.htmlsafe_dumps(get_todo_by_id_controler({"_id" : int(id)}))

# http://localhost:5000/api/todo  method = POST
@todo.route('/api/todo', methods=['POST'])
def add_todo():
    id = request.json['_id']
    name = request.json['name']
    age  =request.json['age']
    data = {"_id": id, "name": name, "age": age}
    add_todo_controller(data)
    return "ok"

# http://localhost:5000/api/todo/?_id=3  method = PUT
@todo.route('/api/todo/', methods=['PUT'])
def put_todo():
    id  = request.args['_id']
    name = request.json['name']
    age  =request.json['age']
    update_todo_controller({"name":name, "age":age,"_id":int(id)})
    print(id)
    return 'ok'

# http://localhost:5000/api/todo/?_id=4  method = DELETE
@todo.route('/api/todo/', methods=['DELETE'])
def delete_todo():
    id  = request.args['_id']
    delete_todo_controller({"_id":int(id)})
    return 'ok'

