from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Shelter, db
from app.api import bp


@bp.route("/shelters", methods=["GET"])
@jwt_required()
def get_shelters():
    shelters = Shelter.query.all()
    return jsonify(
        [
            {
                "id": shelter.id,
                "name": shelter.name,
                "description": shelter.description,
                "location_id": shelter.location_id,
                "contact_info": shelter.contact_info,
            }
            for shelter in shelters
        ]
    )


@bp.route("/shelters/<int:shelter_id>", methods=["GET"])
@jwt_required()
def get_shelter(shelter_id):
    shelter = Shelter.query.get_or_404(shelter_id)
    return jsonify(
        {
            "id": shelter.id,
            "name": shelter.name,
            "description": shelter.description,
            "location_id": shelter.location_id,
            "contact_info": shelter.contact_info,
        }
    )


@bp.route("/shelters", methods=["POST"])
@jwt_required()
def create_shelter():
    data = request.get_json()
    shelter = Shelter(
        name=data["name"],
        description=data["description"],
        location_id=data["location_id"],
        contact_info=data["contact_info"],
    )
    db.session.add(shelter)
    db.session.commit()
    return (
        jsonify(
            {
                "id": shelter.id,
                "name": shelter.name,
                "description": shelter.description,
                "location_id": shelter.location_id,
                "contact_info": shelter.contact_info,
            }
        ),
        201,
    )


@bp.route("/shelters/<int:shelter_id>", methods=["PUT"])
@jwt_required()
def update_shelter(shelter_id):
    shelter = Shelter.query.get_or_404(shelter_id)
    data = request.get_json()
    shelter.name = data.get("name", shelter.name)
    shelter.description = data.get("description", shelter.description)
    shelter.location_id = data.get("location_id", shelter.location_id)
    shelter.contact_info = data.get("contact_info", shelter.contact_info)
    db.session.commit()
    return jsonify(
        {
            "id": shelter.id,
            "name": shelter.name,
            "description": shelter.description,
            "location_id": shelter.location_id,
            "contact_info": shelter.contact_info,
        }
    )


@bp.route("/shelters/<int:shelter_id>", methods=["DELETE"])
@jwt_required()
def delete_shelter(shelter_id):
    shelter = Shelter.query.get_or_404(shelter_id)
    db.session.delete(shelter)
    db.session.commit()
    return jsonify({"msg": "Shelter deleted"}), 200
