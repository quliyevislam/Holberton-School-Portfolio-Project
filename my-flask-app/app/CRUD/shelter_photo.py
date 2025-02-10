from ..models import db, ShelterPhoto

def create_shelter_photo(id, shelter_id, photo):
    shelter_photo = ShelterPhoto(id=id, shelter_id=shelter_id, photo=photo)
    db.session.add(shelter_photo)
    db.session.commit()
    return shelter_photo

def get_all_photos():
    return ShelterPhoto.query.all()

def get_photo_by_shelter_id(shelter_id):
    photo = ShelterPhoto.query.filter_by(shelter_id=shelter_id).first()
    return photo

def update_photo(id, shelter_id, photo):
    photo = ShelterPhoto.query.filter_by(id=id).first()
    photo.shelter_id = shelter_id
    photo.photo = photo
    db.session.commit()
    return photo

def delete_photo(shelter_id):
    photo = ShelterPhoto.query.filter_by(shelter_id=shelter_id).first()
    db.session.delete(photo)
    db.session.commit()
    return photo
