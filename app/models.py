from . import db
import datetime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    shelter_id = db.Column(db.Integer(), db.ForeignKey("shelters.id"))
    clinic_id = db.Column(db.Integer())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    updated_at = db.Column(
        db.DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now
    )

    def __repr__(self):
        return "<User '{}'>".format(self.name)


class ShelterAccount(db.Model):
    __tablename__ = "shelter_accounts"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    shelter_id = db.Column(db.Integer(), db.ForeignKey("shelters.id"), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )

    def __repr__(self):
        return "<ShelterAccount '{}'>".format(self.email)


class Shelter(db.Model):
    __tablename__ = "shelters"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())
    location_id = db.Column(db.Integer(), db.ForeignKey("locations.id"))
    contact_info = db.Column(db.String(255))

    users = db.relationship("User", backref="shelter", lazy="dynamic")
    shelter_account = db.relationship(
        "ShelterAccount", backref="shelter", lazy="joined"
    )
    animals = db.relationship("AnimalShelter", backref="shelter", lazy="dynamic")
    photos = db.relationship("ShelterPhoto", backref="shelter", lazy="dynamic")

    def __repr__(self):
        return "<Shelter '{}'>".format(self.name)


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text())
    info = db.Column(db.Text())

    shelters = db.relationship("Shelter", backref="location", lazy="dynamic")

    def __repr__(self):
        return "<Location '{}'>".format(self.name)


class AnimalShelter(db.Model):
    __tablename__ = "animals_shelter"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer())
    breed = db.Column(db.String(255))
    description = db.Column(db.Text())
    status = db.Column(db.String(255))
    animal_type = db.Column(db.String(10), nullable=False)  # 'dog' or 'cat'
    shelter_id = db.Column(db.Integer(), db.ForeignKey("shelters.id"))

    photos = db.relationship("AnimalPhoto", backref="animal", lazy="dynamic")

    def __repr__(self):
        return f"<AnimalShelter '{self.name}' ({self.animal_type})>"


class AnimalPhoto(db.Model):
    __tablename__ = "photos_animal"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    animal_id = db.Column(db.Integer(), db.ForeignKey("animals_shelter.id"))
    url = db.Column(db.Text())

    def __repr__(self):
        return f"<AnimalPhoto '{self.url[:15]}'>"


class ShelterPhoto(db.Model):
    __tablename__ = "shelter_photos"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    shelter_id = db.Column(db.Integer(), db.ForeignKey("shelters.id"))
    url = db.Column(db.Text())

    def __repr__(self):
        return "<ShelterPhoto '{}'>".format(self.url[:15])


class AnimalReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    animal_type = db.Column(db.String(50), nullable=False)
    color_markings = db.Column(db.String(255), nullable=True)
    age = db.Column(db.String(50), nullable=True)
    health_status = db.Column(db.String(255), nullable=True)
    behavior = db.Column(db.String(255), nullable=True)
    injuries = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=False)
    date_found = db.Column(db.Date, nullable=False)
    time_found = db.Column(db.Time, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
