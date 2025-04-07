from ..models import db, AnimalShelter

def create_animal(name, age, breed, description, status, type, shelter_id):
    animal = AnimalShelter(
        name=name, age=age, breed=breed, description=description,
        status=status, type=type, shelter_id=shelter_id
    )
    db.session.add(animal)
    db.session.commit()
    return animal

def get_all_animals():
    return AnimalShelter.query.all()

def get_animal_by_id(animal_id):
    return AnimalShelter.query.get_or_404(animal_id)

def update_animal(animal_id, name, age, breed, description, status, type, shelter_id):
    animal = AnimalShelter.query.get_or_404(animal_id)
    animal.name = name
    animal.age = age
    animal.breed = breed
    animal.description = description
    animal.status = status
    animal.type = type
    animal.shelter_id = shelter_id
    db.session.commit()
    return animal

def delete_animal(animal_id):
    animal = AnimalShelter.query.get_or_404(animal_id)
    db.session.delete(animal)
    db.session.commit()
    return animal
