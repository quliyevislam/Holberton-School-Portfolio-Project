from flask import jsonify, request
from flask_jwt_extended import jwt_required
from app.models import Location, db
from app.api import bp


@bp.route("/locations", methods=["GET"])
@jwt_required()
def get_locations():
    locations = Location.query.all()
    return jsonify(
        [
            {
                "id": location.id,
                "name": location.name,
                "description": location.description,
            }
            for location in locations
        ]
    )


@bp.route("/locations/<int:location_id>", methods=["GET"])
@jwt_required()
def get_location(location_id):
    location = Location.query.get_or_404(location_id)
    return jsonify(
        {"id": location.id, "name": location.name, "description": location.description}
    )


@bp.route("/locations", methods=["POST"])
@jwt_required()
def create_location():
    data = request.get_json()
    location = Location(
        name=data["name"], description=data["description"], info=data["info"]
    )
    db.session.add(location)
    db.session.commit()
    return (
        jsonify(
            {
                "id": location.id,
                "name": location.name,
                "description": location.description,
            }
        ),
        201,
    )


@bp.route("/locations/<int:location_id>", methods=["PUT"])
@jwt_required()
def update_location(location_id):
    location = Location.query.get_or_404(location_id)
    data = request.get_json()
    location.name = data["name"]
    location.description = data["description"]
    location.info = data["info"]
    db.session.commit()
    return jsonify(
        {"id": location.id, "name": location.name, "description": location.description}
    )


@bp.route("/locations/<int:location_id>", methods=["DELETE"])
@jwt_required()
def delete_location(location_id):
    location = Location.query.get_or_404(location_id)
    db.session.delete(location)
    db.session.commit()
    return jsonify({"msg": "Location deleted"}), 200
