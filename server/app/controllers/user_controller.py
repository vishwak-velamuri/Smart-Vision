from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_controller = Blueprint('user', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_controller.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404