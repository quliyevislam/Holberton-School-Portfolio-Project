from flask import Flask
from config import DevConfig
from flask_migrate import Migrate
from models import db
from models import User, Shelter, Location, ShelterAccount, ShelterPhoto, CatShelter, PhotoShelterCat, PhotoShelterDog, DogShelter

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)
migrate = Migrate(app, db)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()