from flask_sqlalchemy import SQLAlchemy
from models import db, User, ShelterAccount, Shelter, CatShelter, DogShelter, Location
from .user import *
from .shelter_account import *
from .shelter_list import *
from .cat_shelter import *
from .dog_shelter import *
from .location import *
from .photo_shelter_cat import *
from .photo_shelter_dog import *
from .shelter_photo import *

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()