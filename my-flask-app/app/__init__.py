import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from . import routes, models
        # Ensure all models are imported
        from .models import User, ShelterAccount, Shelter, Location, CatShelter, DogShelter, PhotoShelterCat, PhotoShelterDog, ShelterPhoto

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app