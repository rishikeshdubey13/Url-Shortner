from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth = Blueprint("auth",__name__)


@auth.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error":"Username and password is required"}), 400
    
    existing_user = User.query.filter_by(username =username).first()
    if existing_user:
        return jsonify({"error": "Username already exists"}),400
    
    new_user = User(username= username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})

@auth.route("/login", methods = ['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username = username).first()

    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid Credentials"}),401
    
    access_token =create_access_token(identity =user.id)
    return jsonify({"access_token":access_token}),200







