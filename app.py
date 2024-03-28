from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
from resources.user import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, '/register', methods =['GET','POST'])


if __name__=="__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)
