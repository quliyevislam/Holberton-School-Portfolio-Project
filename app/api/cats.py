from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.models import CatShelter, db
from app.api import bp


@bp.route("/cats", methods=["GET"])
@jwt_required()
def get_cats():
    cats = CatShelter.query.all()
    return jsonify(
        [
            {
                "id": cat.id,
                "name": cat.name,
                "age": cat.age,
                "breed": cat.breed,
                "description": cat.description,
                "status": cat.status,
                "shelter_id": cat.shelter_id,
            }
            for cat in cats
        ]
    )


@bp.route("/cats/<int:cat_id>", methods=["GET"])
@jwt_required()
def get_cat(cat_id):
    cat = CatShelter.query.get_or_404(cat_id)
    return jsonify(
        {
            "id": cat.id,
            "name": cat.name,
            "age": cat.age,
            "breed": cat.breed,
            "description": cat.description,
            "status": cat.status,
            "shelter_id": cat.shelter_id,
        }
    )


@bp.route("/cats", methods=["POST"])
@jwt_required()
def create_cat():
    data = request.get_json()
    cat = CatShelter(
        name=data["name"],
        age=data["age"],
        breed=data["breed"],
        description=data["description"],
        status=data["status"],
        shelter_id=data["shelter_id"],
    )
    db.session.add(cat)
    db.session.commit()
    return (
        jsonify(
            {
                "id": cat.id,
                "name": cat.name,
                "age": cat.age,
                "breed": cat.breed,
                "description": cat.description,
                "status": cat.status,
                "shelter_id": cat.shelter_id,
            }
        ),
        201,
    )


@bp.route("/cats/<int:cat_id>", methods=["PUT"])
@jwt_required()
def update_cat(cat_id):
    cat = CatShelter.query.get_or_404(cat_id)
    data = request.get_json()
    cat.name = data.get("name", cat.name)
    cat.age = data.get("age", cat.age)
    cat.breed = data.get("breed", cat.breed)
    cat.description = data.get("description", cat.description)
    cat.status = data.get("status", cat.status)
    cat.shelter_id = data.get("shelter_id", cat.shelter_id)
    db.session.commit()
    return jsonify(
        {
            "id": cat.id,
            "name": cat.name,
            "age": cat.age,
            "breed": cat.breed,
            "description": cat.description,
            "status": cat.status,
            "shelter_id": cat.shelter_id,
        }
    )


@bp.route("/cats/<int:cat_id>", methods=["DELETE"])
@jwt_required()
def delete_cat(cat_id):
    cat = CatShelter.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    return jsonify({"msg": "Cat deleted"}), 200
