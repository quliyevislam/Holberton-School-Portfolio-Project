from ..models import db, PhotoShelterCat

def create_photo_shelter_cat(id, animal_id, animal_type, url):
    photo_shelter_cat = PhotoShelterCat(id=id, animal_id=animal_id, animal_type=animal_type, url=url)
    db.session.add(photo_shelter_cat)
    db.session.commit()
    return photo_shelter_cat

def get_all_photos():
    return PhotoShelterCat.query.all()

def get_photo_by_animal_id(animal_id):
    photo = PhotoShelterCat.query.filter_by(animal_id=animal_id).first()
    return photo

def update_photo(id, animal_id, animal_type, url):
    photo = PhotoShelterCat.query.filter_by(id=id).first()
    photo.animal_id = animal_id
    photo.animal_type = animal_type
    photo.url = url
    db.session.commit()
    return photo

def delete_photo(animal_id):
    photo = PhotoShelterCat.query.filter_by(animal_id=animal_id).first()
    db.session.delete(photo)
    db.session.commit()
    return photo