from .extensions import db

def get_all_todo():
    return [doc for doc in db.get_collection('todo').find({})]

def createId():
    arr = [doc for doc in db.get_collection('todo').find({})]
    return arr[len(arr)-1]['_id']

def get_todo_by_id_controler(todo):
    return db.get_collection('todo').find_one({"_id" : todo['_id']})

def add_todo_controller(todo): 
    return db.get_collection('todo').insert(todo)

def update_todo_controller(todo):
    return db.get_collection('todo').find_one_and_update({'_id': todo['_id']},{'$set':todo})

def delete_todo_controller(todo):
    return db.get_collection('todo').delete_one({'_id':todo['_id']})



