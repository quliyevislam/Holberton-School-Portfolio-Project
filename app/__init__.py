import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()

from app.CRUD.user import create_admin_user


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    login_manager.login_message = "Please log in to access this page."
    CORS(app, supports_credentials=True)

    if not os.path.exists("logs"):
        os.mkdir("logs")
        file_handler = RotatingFileHandler(
            "logs/shelter.log", maxBytes=10240, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Shelter startup")

    from app.main import bp as main_blueprint

    app.register_blueprint(main_blueprint)

    from app.errors import bp as errors_blueprint

    app.register_blueprint(errors_blueprint)

    return app


from app import models
