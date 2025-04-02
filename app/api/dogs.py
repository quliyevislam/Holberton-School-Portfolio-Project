from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.models import DogShelter, db
from app.api import bp


@bp.route("/dogs", methods=["GET"])
@jwt_required()
def get_dogs():
    dogs = DogShelter.query.all()
    return jsonify(
        [
            {
                "id": dog.id,
                "name": dog.name,
                "age": dog.age,
                "breed": dog.breed,
                "description": dog.description,
                "status": dog.status,
                "shelter_id": dog.shelter_id,
            }
            for dog in dogs
        ]
    )


@bp.route("/dogs/<int:dog_id>", methods=["GET"])
@jwt_required()
def get_dog(dog_id):
    dog = DogShelter.query.get_or_404(dog_id)
    return jsonify(
        {
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
            "description": dog.description,
            "status": dog.status,
            "shelter_id": dog.shelter_id,
        }
    )


@bp.route("/dogs", methods=["POST"])
@jwt_required()
def create_dog():
    data = request.get_json()
    dog = DogShelter(
        name=data["name"],
        age=data["age"],
        breed=data["breed"],
        description=data["description"],
        status=data["status"],
        shelter_id=data["shelter_id"],
    )
    db.session.add(dog)
    db.session.commit()
    return (
        jsonify(
            {
                "id": dog.id,
                "name": dog.name,
                "age": dog.age,
                "breed": dog.breed,
                "description": dog.description,
                "status": dog.status,
                "shelter_id": dog.shelter_id,
            }
        ),
        201,
    )


@bp.route("/dogs/<int:dog_id>", methods=["PUT"])
@jwt_required()
def update_dog(dog_id):
    dog = DogShelter.query.get_or_404(dog_id)
    data = request.get_json()
    dog.name = data.get("name", dog.name)
    dog.age = data.get("age", dog.age)
    dog.breed = data.get("breed", dog.breed)
    dog.description = data.get("description", dog.description)
    dog.status = data.get("status", dog.status)
    dog.shelter_id = data.get("shelter_id", dog.shelter_id)
    db.session.commit()
    return jsonify(
        {
            "id": dog.id,
            "name": dog.name,
            "age": dog.age,
            "breed": dog.breed,
            "description": dog.description,
            "status": dog.status,
            "shelter_id": dog.shelter_id,
        }
    )


@bp.route("/dogs/<int:dog_id>", methods=["DELETE"])
@jwt_required()
def delete_dog(dog_id):
    dog = DogShelter.query.get_or_404(dog_id)
    db.session.delete(dog)
    db.session.commit()
    return jsonify({"msg": "Dog deleted"}), 200
