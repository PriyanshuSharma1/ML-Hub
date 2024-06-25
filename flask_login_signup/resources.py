from flask_restful import Resource, reqparse
from models import UserModel
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class UserResource(Resource):
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return {"username": user.username, "password": user.password}
        return {"message": "User not found"}, 404

    def post(self, username):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True, help="Password cannot be blank!")
        data = parser.parse_args()
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user = UserModel(username, hashed_password)
        user.save_to_db()
        return {"message": "User created successfully"}, 201

