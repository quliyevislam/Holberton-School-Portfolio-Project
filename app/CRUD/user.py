from app.models import db, User
from werkzeug.security import generate_password_hash
import logging

logger = logging.getLogger(__name__)

def create_new_user(name, email, password, shelter_id=None):
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password, shelter_id=shelter_id)
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

def create_admin_user():
    admin_email = "admin@example.com"
    admin_password = "adminpassword"
    if not User.query.filter_by(email=admin_email).first():
        hashed_password = generate_password_hash(admin_password)
        admin_user = User(name="Admin", email=admin_email, password=hashed_password)
        db.session.add(admin_user)
        db.session.commit()
        logger.debug(f"Admin user created with email: {admin_email}")
    else:
        logger.debug(f"Admin user already exists with email: {admin_email}")
