from run import db
import datetime

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    shelter_id = db.Column(db.BigInteger(), db.ForeignKey('shelters.id'))
    clinic_id = db.Column(db.BigInteger())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return "<User '{}'>".format(self.name)

class ShelterAccount(db.Model):
    __tablename__ = 'shelter_accounts'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    shelter_id = db.Column(db.BigInteger(), db.ForeignKey('shelters.id'))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return "<ShelterAccount '{}'>".format(self.email)

class Shelter(db.Model):
    __tablename__ = 'shelters'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text())
    location_id = db.Column(db.BigInteger(), db.ForeignKey('locations.id'))
    contact_info = db.Column(db.String(255))
    
    users = db.relationship(
        'User',
        backref='shelter',
        lazy='dynamic'
    )
    shelter_account = db.relationship(
        'ShelterAccount',
        backref='shelter',
        lazy='joined'
    )
    cats = db.relationship(
        'CatShelter',
        backref='shelter',
        lazy='dynamic'
    )
    dogs = db.relationship(
        'DogShelter',
        backref='shelter',
        lazy='dynamic'
    )
    photos = db.relationship(
        'ShelterPhoto',
        backref='shelter',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<Shelter '{}'>".format(self.name)

class Location(db.Model):
    __tablename__ = 'locations'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    description = db.Column(db.Text())
    info = db.Column(db.Text())
    
    shelters = db.relationship(
        'Shelter',
        backref='location',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<Location '{}'>".format(self.name)

class CatShelter(db.Model):
    __tablename__ = 'cats_shelter'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer())
    breed = db.Column(db.String(255))
    description = db.Column(db.Text())
    status = db.Column(db.String(255))
    shelter_id = db.Column(db.BigInteger(), db.ForeignKey('shelters.id'))
    
    photos = db.relationship(
        'PhotoShelterCat',
        backref='cat',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<CatShelter '{}'>".format(self.name)

class DogShelter(db.Model):
    __tablename__ = 'dogs_shelter'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer())
    breed = db.Column(db.String(255))
    description = db.Column(db.Text())
    status = db.Column(db.String(255))
    shelter_id = db.Column(db.BigInteger(), db.ForeignKey('shelters.id'))
    
    photos = db.relationship(
        'PhotoShelterDog',
        backref='dog',
        lazy='dynamic'
    )

    def __repr__(self):
        return "<DogShelter '{}'>".format(self.name)

class PhotoShelterCat(db.Model):
    __tablename__ = 'photos_shelter_cat'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    animal_id = db.Column(db.BigInteger(), db.ForeignKey('cats_shelter.id'))
    animal_type = db.Column(db.Enum('cat'), default='cat')
    url = db.Column(db.Text())

    def __repr__(self):
        return "<PhotoShelterCat '{}'>".format(self.url[:15])

class PhotoShelterDog(db.Model):
    __tablename__ = 'photos_shelter_dog'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    animal_id = db.Column(db.BigInteger(), db.ForeignKey('dogs_shelter.id'))
    animal_type = db.Column(db.Enum('dog'), default='dog')
    url = db.Column(db.Text())

    def __repr__(self):
        return "<PhotoShelterDog '{}'>".format(self.url[:15])

class ShelterPhoto(db.Model):
    __tablename__ = 'shelter_photos'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    shelter_id = db.Column(db.BigInteger(), db.ForeignKey('shelters.id'))
    url = db.Column(db.Text())

    def __repr__(self):
        return "<ShelterPhoto '{}'>".format(self.url[:15])