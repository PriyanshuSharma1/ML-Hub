import os
from pymongo import MongoClient

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_URI = "mongodb://localhost:27017/login_signup_db"
    @staticmethod
    def check_connection():
        try:
            client = MongoClient(Config.MONGO_URI)
            db = client.get_default_database()
            db.command("ping")
            print("Connection established successfully!")
        except Exception as e:
            print(f"Connection failed: {e}")

Config.check_connection()
print(Config.SECRET_KEY)