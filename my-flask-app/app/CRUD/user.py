from ..models import User, db

def create_user(id, name, email, password, shelter_id, clinic_id):
    user = User(id=id, name=name, email=email, password=password, shelter_id=shelter_id, clinic_id=clinic_id)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.all()

def get_user_by_name(name):
    user = User.query.filter_by(name=name).first()
    return user

def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    return user

def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user

def update_user(id, name, email, password, shelter_id, clinic_id):
    user = User.query.filter_by(id=id).first()
    user.name = name
    user.email = email
    user.password = password
    user.shelter_id = shelter_id
    user.clinic_id = clinic_id
    db.session.commit()
    return user

def delete_user(name):
    user = User.query.filter_by(name=name).first()
    db.session.delete(user)
    db.session.commit()
    return user
