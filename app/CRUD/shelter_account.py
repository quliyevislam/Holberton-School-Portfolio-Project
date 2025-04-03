from app.models import db, ShelterAccount

def create_new_shelter_account(name, email, password, location_id=None):
    shelter_account = ShelterAccount(name=name, email=email, password=password)
    if location_id:
        shelter = Shelter.query.filter_by(location_id=location_id).first()
        if shelter:
            shelter_account.shelter_id = shelter.id
    db.session.add(shelter_account)
    db.session.commit()
    return shelter_account

def get_all_shelter_accounts():
    return ShelterAccount.query.all()

def get_shelter_account_by_name(name):
    shelter_account = ShelterAccount.query.filter_by(name=name).first()
    return shelter_account

def get_shelter_account_by_id(id):
    shelter_account = ShelterAccount.query.filter_by(id=id).first()
    return shelter_account

def update_shelter_account(id, name, email, password):
    shelter_account = ShelterAccount.query.filter_by(id=id).first()
    shelter_account.name = name
    shelter_account.email = email
    shelter_account.password = password
    db.session.commit()
    return shelter_account

def delete_shelter_account_by_id(id):
    shelter_account = ShelterAccount.query.filter_by(id=id).first()
    db.session.delete(shelter_account)
    db.session.commit()