from flask import render_template, request, redirect, url_for, flash, Flask, jsonify
from app.main import bp as main
from app.models import db, User, Shelter
from app.CRUD.location import create_new_location, get_location_by_id, update_location_by_id, delete_location_by_id, get_all_locations
from app.CRUD.user import create_new_user, get_user_by_id, update_user_by_id, delete_user_by_id, get_all_users, create_admin_user
from app.CRUD.shelter_account import create_new_shelter_account, get_all_shelter_accounts, get_shelter_account_by_id, update_shelter_account, delete_shelter_account_by_id
from app.CRUD.cat_shelter import create_cat_shelter, get_all_cats, get_cat_by_id, update_cat, delete_cat
from app.CRUD.dog_shelter import create_dog_shelter, get_all_dogs, get_dog_by_id, update_dog, delete_dog
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import Config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

@main.route('/')
def home():
    return render_template('home.html')
@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('features/contact.html')

@main.route('/report_animal')
def report():
    return render_template('features/report.html')

@main.route('/map')
def map():
    return render_template('features/map.html')

@main.route('/chat')
def chat():
    return render_template('features/chat.html')

@main.route('/community')
def community():
    return render_template('features/community.html')

@main.route('/donate')
def donate():
    return render_template('features/donate.html')

@main.route('/location/<int:location_id>', methods=['GET'])
def location(location_id):
    location = get_location_by_id(location_id)
    return render_template('location/location.html', location=location)

@main.route('/location/create_location', methods=['GET', 'POST'])
@jwt_required()
def create_location():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        info = request.form['info']
        create_new_location(name=name, description=description, info=info)
        return redirect(url_for('main.location_list'))
    return render_template('location/create_location.html')

@main.route('/location/update/<int:location_id>', methods=['GET', 'POST'])
@jwt_required()
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
@jwt_required()
def delete_location(location_id):
    delete_location_by_id(location_id)
    return redirect(url_for('main.location_list'))

@main.route('/locations', methods=['GET'])
def location_list():
    locations = get_all_locations()
    return render_template('location/location_list.html', locations=locations)

@main.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return render_template('user/users_list.html', users=users)

@main.route('/user/<int:user_id>', methods=['GET'])
@jwt_required()
def user(user_id):
    user = get_user_by_id(user_id)
    return render_template('user/user.html', user=user)

@main.route('/user/create_user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please use a different email.', 'danger')
            return redirect(url_for('main.create_user'))
        create_new_user(name=request.form['name'], email=email, password=password)
        return redirect(url_for('main.get_users'))
    return render_template('user/create_user.html')

@main.route('/user/update/<int:user_id>', methods=['GET', 'POST'])
@jwt_required()
def update_user(user_id):
    user = get_user_by_id(user_id)
    if request.method == 'POST':
        update_user_by_id(user_id, name=request.form.get('name'), email=request.form.get('email'))
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.user', user_id=user.id))
    return render_template('user/update_user.html', user=user)

@main.route('/user/delete/<int:user_id>', methods=['POST'])
@jwt_required()
def delete_user(user_id):
    delete_user_by_id(user_id)
    flash('User deleted successfully!', 'success')
    return redirect(url_for('main.get_users'))

@main.route('/shelter_account/<int:shelter_account_id>', methods=['GET'])
def shelter_account(shelter_account_id):
    shelter_account = get_shelter_account_by_id(shelter_account_id)
    return render_template('shelter_account/shelter_account.html', shelter_account=shelter_account)

@main.route('/shelter_account/update/<int:shelter_account_id>', methods=['GET', 'POST'])
@jwt_required()
def update_shelter_account_route(shelter_account_id):
    shelter_account = get_shelter_account_by_id(shelter_account_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        update_shelter_account(shelter_account_id, name, email, password)
        flash('Shelter account updated successfully!', 'success')
        return redirect(url_for('main.shelter_account', shelter_account_id=shelter_account_id))
    return render_template('shelter_account/update_shelter_account.html', shelter_account=shelter_account)

@main.route('/shelter_account/delete/<int:shelter_account_id>', methods=['POST'])
@jwt_required()
def delete_shelter_account_route(shelter_account_id):
    delete_shelter_account_by_id(shelter_account_id)
    flash('Shelter account deleted successfully!', 'success')
    return redirect(url_for('main.shelter_account_list'))

@main.route('/shelter_account_list', methods=['GET'])
def shelter_account_list():
    shelter_accounts = get_all_shelter_accounts()
    return render_template('shelter_account/shelter_account_list.html', shelter_accounts=shelter_accounts)

@main.route('/shelter_account/create', methods=['GET', 'POST'])
@jwt_required()
def create_shelter_account():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            shelter_account = create_new_shelter_account(name=name, email=email, password=password)
            flash('Shelter account created successfully!', 'success')
            return redirect(url_for('main.shelter_account', shelter_account_id=shelter_account.id))
        except ValueError as e:
            flash(str(e), 'danger')
    return render_template('shelter_account/create_shelter_account.html')

@main.route('/cats', methods=['GET'])
def cat_list():
    cats = get_all_cats()
    return render_template('shelter_cat/shelter_cat_list.html', cats=cats)

@main.route('/cat/<int:cat_id>', methods=['GET'])
def cat(cat_id):
    cat = get_cat_by_id(cat_id)
    return render_template('shelter_cat/shelter_cat.html', cat=cat)

@main.route('/cat/create', methods=['GET', 'POST'])
@jwt_required()
def create_cat():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        breed = request.form.get('breed')
        description = request.form.get('description')
        status = request.form.get('status')
        shelter_id = request.form.get('shelter_id')

        if not all([name, age, breed, description, status, shelter_id]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('main.create_cat'))

        shelter = Shelter.query.get(shelter_id)
        if not shelter:
            flash('Shelter ID does not exist. Please provide a valid Shelter ID.', 'danger')
            return redirect(url_for('main.create_cat'))

        create_cat_shelter(id=None, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
        flash('Cat created successfully!', 'success')
        return redirect(url_for('main.cat_list'))
    return render_template('shelter_cat/shelter_cat_create.html')

@main.route('/cat/update/<int:cat_id>', methods=['GET', 'POST'])
@jwt_required()
def update_cat_route(cat_id):
    cat = get_cat_by_id(cat_id)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        breed = request.form['breed']
        description = request.form['description']
        status = request.form['status']
        shelter_id = request.form['shelter_id']
        update_cat(id=cat_id, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
        return redirect(url_for('main.cat', cat_id=cat_id))
    return render_template('shelter_cat/shelter_cat_update.html', cat=cat)

@main.route('/cat/delete/<int:cat_id>', methods=['POST'])
@jwt_required()
def delete_cat_route(cat_id):
    delete_cat(cat_id)
    return redirect(url_for('main.cat_list'))

@main.route('/dogs', methods=['GET'])
def dog_list():
    dogs = get_all_dogs()
    return render_template('shelter_dog/shelter_dog_list.html', dogs=dogs)

@main.route('/dog/<int:dog_id>', methods=['GET'])
def dog(dog_id):
    dog = get_dog_by_id(dog_id)
    return render_template('shelter_dog/shelter_dog.html', dog=dog)

@main.route('/dog/create', methods=['GET', 'POST'])
@jwt_required()
def create_dog():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        breed = request.form.get('breed')
        description = request.form.get('description')
        status = request.form.get('status')
        shelter_id = request.form.get('shelter_id')

        if not all([name, age, breed, description, status, shelter_id]):
            flash('All fields are required.', 'danger')
            return redirect(url_for('main.create_dog'))

        shelter = Shelter.query.get(shelter_id)
        if not shelter:
            flash('Shelter ID does not exist. Please provide a valid Shelter ID.', 'danger')
            return redirect(url_for('main.create_dog'))

        create_dog_shelter(id=None, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
        flash('Dog created successfully!', 'success')
        return redirect(url_for('main.dog_list'))
    return render_template('shelter_dog/shelter_dog_create.html')

@main.route('/dog/update/<int:dog_id>', methods=['GET', 'POST'])
@jwt_required()
def update_dog_route(dog_id):
    dog = get_dog_by_id(dog_id)
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        breed = request.form['breed']
        description = request.form['description']
        status = request.form['status']
        shelter_id = request.form['shelter_id']
        update_dog(id=dog_id, name=name, age=age, breed=breed, description=description, status=status, shelter_id=shelter_id)
        return redirect(url_for('main.dog', dog_id=dog_id))
    return render_template('shelter_dog/shelter_dog_update.html', dog=dog)

@main.route('/dog/delete/<int:dog_id>', methods=['POST'])
@jwt_required()
def delete_dog_route(dog_id):
    delete_dog(dog_id)
    return redirect(url_for('main.dog_list'))

@main.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = get_user_by_id(current_user_id)
    return jsonify(logged_in_as=user.email), 200

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            shelter_id = data.get('shelter_id')

            logger.debug(f"Received signup request with email: {email}")

            if not name or not email or not password:
                logger.debug("Missing required fields")
                return jsonify({"msg": "Missing required fields"}), 400

            if password != confirm_password:
                logger.debug("Passwords do not match")
                return jsonify({"msg": "Passwords do not match"}), 400

            if User.query.filter_by(email=email).first():
                logger.debug(f"Signup attempt with already registered email: {email}")
                return jsonify({"msg": "Email already registered"}), 409

            create_new_user(name=name, email=email, password=password, shelter_id=shelter_id)

            logger.debug(f"User created successfully with email: {email}")
            return jsonify({"msg": "User created successfully"}), 201
        else:
            logger.debug("Request must be JSON")
            return jsonify({"msg": "Request must be JSON"}), 415
    return render_template('auth/sign_up.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return jsonify({"msg": "Missing email or password"}), 400

            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                access_token = create_access_token(identity=user.id)
                return jsonify({"access_token": access_token}), 200

            shelter_admin = shelter_account.query.filter_by(email=email).first()
            
            if shelter_admin and check_password_hash(shelter_admin.password, password):
                access_token = create_access_token(identity=f"admin-{shelter_admin.id}")
                return jsonify({"access_token": access_token}), 200

            return jsonify({"msg": "Invalid email or password"}), 401
        else:
            return jsonify({"msg": "Request must be JSON"}), 415
    return render_template('auth/login.html')

@main.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_identity = get_jwt_identity()

    if str(current_identity).startswith("admin-"):
        admin_id = int(current_identity.split("-")[1])
        admin = shelter_account.query.get(admin_id)
        if admin:
            return jsonify({"msg": "Welcome, Admin!", "admin_email": admin.email}), 200
    else:
        return jsonify({"msg": "Access forbidden"}), 403