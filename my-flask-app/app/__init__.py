import os
import logging
from flask import Flask, render_template
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

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    @app.errorhandler(404)
    def not_found_error(error):
        logger.error(f"404 Not Found Error: {error}")
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"500 Internal Server Error: {error}")
        return render_template('errors/500.html'), 500

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        from . import models

    return app