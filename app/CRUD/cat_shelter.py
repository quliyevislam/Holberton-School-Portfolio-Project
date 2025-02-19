from ..models import CatShelter, db

def create_cat_shelter(id, name, age, breed, description, status, shelter_id):
    cat = CatShelter(id=id, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
    db.session.add(cat)
    db.session.commit()
    return cat

def get_all_cats():
    return CatShelter.query.all()

def get_cat_by_name(name):
    cat = CatShelter.query.filter_by(name=name).first()
    return cat

def get_cat_by_breed(breed):
    cat = CatShelter.query.filter_by(breed=breed).first()
    return cat

def get_cat_by_id(id):
    cat = CatShelter.query.filter_by(id=id).first()
    return cat

def get_cat_by_status(status):
    cat = CatShelter.query.filter_by(status=status).first()
    return cat

def update_cat(id, name, age, breed, description, status, shelter_id):
    cat = CatShelter.query.filter_by(id=id).first()
    cat.name = name
    cat.age = age
    cat.breed = breed
    cat.description = description
    cat.status = status
    cat.shelter_id = shelter_id
    db.session.commit()
    return cat

def delete_cat(name):
    cat = CatShelter.query.filter_by(name=name).first()
    db.session.delete(cat)
    db.session.commit()
    return cat
