from flask import Flask, render_template, Blueprint, request, jsonify, redirect, url_for
from app.models import db, User, Shelter
from app.CRUD.location import create_new_location, get_all_locations, get_location_by_id
import logging

main = Blueprint('main', __name__)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/report_animal')
def report():
    return render_template('report.html')

@main.route('/map')
def map():
    return render_template('map.html')

@main.route('/chat')
def chat():
    return render_template('chat.html')

@main.route('/community')
def community():
    return render_template('community.html')

@main.route('/donate')
def donate():
    return render_template('donate.html')

@main.route('/shelters', methods=['GET'])
def get_shelters():
    shelters = Shelter.query.all()
    return render_template('shelters_list.html', shelters=shelters)

@main.route('/locations', methods=['GET'])
def location_list():
    locations = get_all_locations()
    return render_template('location_list.html', locations=locations)

@main.route('/location/<int:location_id>', methods=['GET'])
def location(location_id):
    location = get_location_by_id(location_id)
    return render_template('location.html', location=location)

@main.route('/create_location', methods=['GET', 'POST'])
def create_location():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        info = request.form['info']
        create_new_location(name=name, description=description, info=info)
        return redirect(url_for('main.location_list'))
    return render_template('create_location.html')

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('users_list.html', users=users)

@main.route('/user/<int:user_id>', methods=['GET'])
def user(user_id):
    user = User.query.get(user_id)
    return render_template('user.html', user=user)

@main.route('/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.get_users'))
    return render_template('create_user.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return redirect(url_for('main.home'))
        else:
            return render_template('sign_in.html', error="Invalid credentials")
    return render_template('sign_in.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password == confirm_password:
            user = User(name=name, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.login'))
        else:
            return render_template('sign_up.html', error="Passwords do not match")
    return render_template('sign_up.html')

