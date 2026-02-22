from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.facade import HBnBFacade

auth_bp = Blueprint('auth', __name__)
facade = HBnBFacade()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = facade.get_user_by_email(email)
    
    if user and user.verify_password(password):
        access_token = create_access_token(identity=user.id, additional_claims={"is_admin": user.is_admin})
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Invalid email or password"}), 401