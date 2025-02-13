from flask import render_template, Blueprint, request, jsonify
from app.models import db, User, Shelter
import logging

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/about')
def about():
    return render_template('about.html')

