from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services.facade import HBnBFacade

place_bp = Blueprint('places', __name__)
facade = HBnBFacade()

@place_bp.route('/', methods=['POST'])
@jwt_required()
def create_place():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    data['owner_id'] = current_user_id
    try:
        new_place = facade.create_place(data)
        return jsonify({"id": new_place.id, "title": new_place.title}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@place_bp.route('/<place_id>', methods=['PUT'])
@jwt_required()
def update_place(place_id):
    current_user_id = get_jwt_identity()
    claims = get_jwt()
    is_admin = claims.get("is_admin", False)
    
    place = facade.get_place(place_id)
    if not place:
        return jsonify({"error": "Place not found"}), 404
        
    if not is_admin and place.owner_id != current_user_id:
        return jsonify({"error": "Unauthorized action"}), 403
        
    data = request.get_json()
    facade.update_place(place_id, data)
    return jsonify({"msg": "Place updated"}), 200