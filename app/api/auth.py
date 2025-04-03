from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models import User, ShelterAccount
from app.api import bp


@bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not all(key in data for key in ("email", "password")):
        return jsonify({"msg": "Missing email or password"}), 400

    email = data.get("email")
    password = data.get("password")

    # Check user credentials
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=f"user-{user.id}")
        return jsonify({"access_token": access_token}), 200

    # Check shelter admin credentials
    shelter_admin = ShelterAccount.query.filter_by(email=email).first()
    if shelter_admin and check_password_hash(shelter_admin.password, password):
        access_token = create_access_token(identity=f"admin-{shelter_admin.id}")
        return jsonify({"access_token": access_token}), 200

    return jsonify({"msg": "Invalid email or password"}), 401


@bp.route("/auth/admin", methods=["GET"])
@jwt_required()
def admin():
    current_identity = get_jwt_identity()

    if str(current_identity).startswith("admin-"):
        admin_id = int(current_identity.split("-")[1])
        admin = ShelterAccount.query.get(admin_id)
        if admin:
            return jsonify({"msg": "Welcome, Admin!", "admin_email": admin.email}), 200

    return jsonify({"msg": "Access forbidden"}), 403
