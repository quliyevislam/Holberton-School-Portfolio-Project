from flask import Flask, render_template, Blueprint, request, jsonify, redirect, url_for, flash
from app.models import db, User, Shelter
from app.CRUD.location import create_new_location, get_location_by_id, update_location_by_id, delete_location_by_id, get_all_locations
import logging
from werkzeug.security import generate_password_hash, check_password_hash

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

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return render_template('user/users_list.html', users=users)

@main.route('/location/<int:location_id>', methods=['GET'])
def location(location_id):
    location = get_location_by_id(location_id)
    return render_template('location/location.html', location=location)

@main.route('/location/create_location', methods=['GET', 'POST'])
def create_location():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        info = request.form['info']
        create_new_location(name=name, description=description, info=info)
        return redirect(url_for('main.location_list'))
    return render_template('create_location.html')

@main.route('/location/update/<int:location_id>', methods=['GET', 'POST'])
def update_location(location_id):
    location = get_location_by_id(location_id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        info = request.form['info']
        update_location_by_id(location_id, name, description, info)
        return redirect(url_for('main.location', location_id=location_id))
    return render_template('location/update_location.html', location=location)

@main.route('/location/delete/<int:location_id>', methods=['POST'])
def delete_location(location_id):
    delete_location_by_id(location_id)
    return redirect(url_for('main.location_list'))

@main.route('/locations', methods=['GET'])
def location_list():
    locations = get_all_locations()
    return render_template('location/location_list.html', locations=locations)

@main.route('/user/<int:user_id>', methods=['GET'])
def user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user/user.html', user=user)

@main.route('/user/create_user', methods=['GET', 'POST'])
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
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.user', user_id=user.id))
        else:
            flash('Login failed. Check your email and password.', 'danger')

    return render_template('auth/sign_in.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('main.signup'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))

    return render_template('auth/sign_up.html')

@main.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        user.name = request.form.get('name')
        user.email = request.form.get('email')
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.user', user_id=user.id))
    return render_template('user/update_user.html', user=user)

@main.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('main.get_users'))

