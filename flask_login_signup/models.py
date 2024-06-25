from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from app import mongo
from app import bcrypt

class UserModel:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_mongo(self):
        db=mongo.db
        user= db.users.find_one({"username":self.username})
        if not user:
            hashed_pw=bcrypt.generate_password_hash(self.password).decode('utf-8')
            db.users.insert_one({"username":self.username,"password":hashed_pw})

@classmethod

def find_user(cls, username):
    db= mongo.db
    user_data= db.users.find_one({"username":username})
    if user_data:
        return cls(user_data["username"],user_data["password"])
    return None
    

