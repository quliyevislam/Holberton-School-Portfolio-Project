from flask import Blueprint

bp = Blueprint("api", __name__)

from app.api import shelters, users, locations, dogs, cats, auth
