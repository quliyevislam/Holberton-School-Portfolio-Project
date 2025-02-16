from app.models import db, User

def create_new_user(name, email, password):
    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def get_user_by_id(user_id):
    return User.query.get_or_404(user_id)

def update_user_by_id(user_id, name, email):
    user = User.query.get_or_404(user_id)
    user.name = name
    user.email = email
    db.session.commit()

def delete_user_by_id(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

def get_all_users():
    return User.query.all()
