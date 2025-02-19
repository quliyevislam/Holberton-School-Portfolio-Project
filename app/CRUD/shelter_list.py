from ..models import db, Shelter

def create_shelter(id, name, description, location_id, contact_info):
    shelter = Shelter(id=id, name=name, description=description, location_id=location_id, contact_info=contact_info)
    db.session.add(shelter)
    db.session.commit()
    return shelter

def get_all_shelters():
    return Shelter.query.all()

def get_shelter_by_name(name):
    shelter = Shelter.query.filter_by(name=name).first()
    return shelter

def get_shelter_by_id(id):
    shelter = Shelter.query.filter_by(id=id).first()
    return shelter

def get_shelter_by_location(location_id):
    shelter = Shelter.query.filter_by(location_id=location_id).first()
    return shelter

def update_shelter(id, name, description, location_id, contact_info):
    shelter = Shelter.query.filter_by(id=id).first()
    shelter.name = name
    shelter.description = description
    shelter.location_id = location_id
    shelter.contact_info = contact_info
    db.session.commit()
    return shelter

def delete_shelter(name):
    shelter = Shelter.query.filter_by(name=name).first()
    db.session.delete(shelter)
    db.session.commit()
    return shelter
