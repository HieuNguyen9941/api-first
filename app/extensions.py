from flask_pymongo import pymongo
from .settings import MONGO_URI

# MONGO_URI='mongodb+srv://Test:12345@cluster0.jrmvt.mongodb.net/todo?retryWrites=true&w=majority'

mongo = pymongo.MongoClient(MONGO_URI)

db = mongo.get_database('todo')