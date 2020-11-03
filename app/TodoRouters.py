from flask import Blueprint, request, json
from .Todo import get_all_todo, add_todo_controller, update_todo_controller, delete_todo_controller,get_todo_by_id_controler
from .JsonEnCode import JSONEncoder
from bson.objectid import ObjectId 

todo = Blueprint('todo', __name__)

# http://localhost:5000/api/todo  method = GET
@todo.route('/api/todo', methods=['GET'])
def get_all():
    return json.htmlsafe_dumps(get_all_todo(),cls=JSONEncoder) 

# http://localhost:5000/api/todo/?id=5f99531d218d5f2074d93120  method = GET
@todo.route('/api/todo/', methods=['GET'])
def get_todo():
    id = request.args['id']
    return json.htmlsafe_dumps(get_todo_by_id_controler({"_id" : ObjectId(id)}),cls=JSONEncoder)

# http://localhost:5000/api/todo  method = POST
@todo.route('/api/todo', methods=['POST'])
def add_todo():
    name = request.json['name']
    age  =request.json['age'] 
    data = {"name": name, "age": age}
    id = add_todo_controller(data)
    data['_id']=id
    return json.htmlsafe_dumps(data,cls=JSONEncoder)

# http://localhost:5000/api/todo  method = PUT
@todo.route('/api/todo', methods=['PUT'])
def put_todo():
    name = request.json['name']
    age  =request.json['age'] 
    id  =request.json['id'] 
    update_todo_controller({"name":name, "age":age,"_id":ObjectId(id)})
    return 'ok'

# http://localhost:5000/api/todo/?id=hjhjhjhj  method = DELETE
@todo.route('/api/todo/', methods=['DELETE'])
def delete_todo():
    id  = request.args['id']
    delete_todo_controller({"_id":ObjectId(id)})
    return 'ok'

