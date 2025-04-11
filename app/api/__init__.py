from flask import Blueprint

bp = Blueprint("api", __name__)

# Avoid importing other modules here to prevent circular imports