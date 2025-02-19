from ..models import db, DogShelter

def create_dog_shelter(id, name, age , breed, description, status, shelter_id):
    dog = DogShelter(id=id, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
    db.session.add(dog)
    db.session.commit()
    return dog

def get_all_dogs():
    return DogShelter.query.all()

def get_dog_by_name(name):
    dog = DogShelter.query.filter_by(name=name).first()
    return dog

def get_dog_by_breed(breed):
    dog = DogShelter.query.filter_by(breed=breed).first()
    return dog

def get_dog_by_id(id):
    dog = DogShelter.query.filter_by(id=id).first()
    return dog

def get_dog_by_status(status):
    dog = DogShelter.query.filter_by(status=status).first()
    return dog

def update_dog(id, name, age, breed, description, status, shelter_id):
    dog = DogShelter.query.filter_by(id=id).first()
    dog.name = name
    dog.age = age
    dog.breed = breed
    dog.description = description
    dog.status = status
    dog.shelter_id = shelter_id
    db.session.commit()
    return dog

def delete_dog(name):
    dog = DogShelter.query.filter_by(name=name).first()
    db.session.delete(dog)
    db.session.commit()
    return dog
