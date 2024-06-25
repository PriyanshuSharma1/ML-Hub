from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_restful import Api
from config import Config
from resources import UserResource, UserListResource


app=Flask(__name__)
app.config.from_object(Config)
mongo=PyMongo(app)
bcrypt=Bcrypt(app)
api=Api(app)


app.config['MONGO_URI']="mongodb://localhost:27017/login_signup_db"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})
        if user and bcrypt.check_password_hash(user['password'], password):
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password', 401
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        mongo.db.users.insert_one({'username': username, 'password': hashed_password})
        return redirect(url_for('login'))
    return render_template('signup.html')



if __name__ == '__main__':
    app.run(debug=True)
