from ..models import db, PhotoShelterDog

def create_photo_shelter_dog(id, animal_id, animal_type, url):
    photo_shelter_dog = PhotoShelterDog(id=id, animal_id=animal_id, animal_type=animal_type, url=url)
    db.session.add(photo_shelter_dog)
    db.session.commit()
    return photo_shelter_dog

def get_all_photos():
    return PhotoShelterDog.query.all()

def get_photo_by_animal_id(animal_id):
    photo = PhotoShelterDog.query.filter_by(animal_id=animal_id).first()
    return photo

def update_photo(id, animal_id, animal_type, url):
    photo = PhotoShelterDog.query.filter_by(id=id).first()
    photo.animal_id = animal_id
    photo.animal_type = animal_type
    photo.url = url
    db.session.commit()
    return photo

def delete_photo(animal_id):
    photo = PhotoShelterDog.query.filter_by(animal_id=animal_id).first()
    db.session.delete(photo)
    db.session.commit()
    return photo
