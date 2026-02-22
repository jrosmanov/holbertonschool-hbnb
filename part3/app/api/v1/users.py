from flask import Blueprint, request, jsonify
from app.services.facade import HBnBFacade

user_bp = Blueprint('users', __name__)
facade = HBnBFacade()

@user_bp.route('/', methods=['POST'])
def register_user():
    user_data = request.get_json()
    
    try:
        new_user = facade.create_user(user_data)
        return jsonify({
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@user_bp.route('/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = facade.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    return jsonify({
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }), 200

@user_bp.route('/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user_id = get_jwt_identity()
    claims = get_jwt()
    
    if current_user_id != user_id and not claims.get("is_admin"):
        return jsonify({"msg": "Administrator access required"}), 403
        
    data = request.get_json()
    data.pop('email', None)
    data.pop('password', None)
    
    facade.update_user(user_id, data)
    return jsonify({"msg": "User updated"}), 200