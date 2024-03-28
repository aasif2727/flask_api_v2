from flask import request,jsonify
from flask_restful import Resource
import bcrypt
from pymongo import MongoClient

client = MongoClient("mongodb+srv://aasif2707:hi6dHwj6jbnLOpVe@cluster0.7ahaiku.mongodb.net/Training?retryWrites=true&w=majority&appName=Cluster0")
db = client["Training"]
users = db["users"]
is_connected = False

class User(Resource):
    @classmethod
    def get(cls):
        try:
            user_list = []
            print(users)
            for user in users.find():
                _email = user.get("Email", "N/A") #to handle missing property
                user_dict = {"Username": user["Username"],"Email": _email,"IsActive" : user["IsActive"]}
                user_list.append(user_dict)
            return jsonify(users=user_list)

        except KeyError as ex:
            return jsonify({'status':500,'message': ex})
    
    @classmethod
    def post(cls):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"] 
        email = postedData.get("email", "N/A") #to handle missing property
        try:
            if users is not None:
                print(users.count_documents({"Username":username}))
                if users.count_documents({"Username":username}) > 0:
                    return jsonify({'status':301,'message': 'Invalid Username'})
                else:
                    hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
                    users.insert_one({ "Username": username,"Password": hashed_pw,"Email":email, "IsActive":1 })
                    return jsonify({'status':200,'message': 'User saved successfully'})
        except KeyError as ex:
            return jsonify({'status':500,'message': ex})
        