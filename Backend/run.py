from flask import Flask
from flask_migrate import Migrate
from models import db
from models import User, Shelter, Location, ShelterAccount, ShelterPhoto, CatShelter, PhotoShelterCat, PhotoShelterDog, DogShelter
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])
migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)