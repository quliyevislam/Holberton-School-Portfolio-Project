from ..models import db, Location

def create_new_location(name, description, info):
    location = Location(name=name, description=description, info=info)
    db.session.add(location)
    db.session.commit()
    return location

def get_all_locations():
    return Location.query.all()

def get_location_by_name(name):
    location = Location.query.filter_by(name=name).first()
    return location

def get_location_by_id(id):
    location = Location.query.filter_by(id=id).first()
    return location

def update_location(id, name, description, info):
    location = Location.query.filter_by(id=id).first()
    location.name = name
    location.description = description
    location.info = info
    db.session.commit()
    return location

def update_location_by_id(id, name, description, info):
    location = Location.query.filter_by(id=id).first()
    if location:
        location.name = name
        location.description = description
        location.info = info
        db.session.commit()
    return location

def delete_location_by_id(id):
    location = Location.query.filter_by(id=id).first()
    if location:
        db.session.delete(location)
        db.session.commit()
    return location
