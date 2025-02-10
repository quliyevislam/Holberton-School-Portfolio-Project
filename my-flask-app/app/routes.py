from flask import render_template, Blueprint, request, jsonify
from app.models import db, User, Shelter
import logging

main = Blueprint('main', __name__)

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

# Маршрут для создания пользователя
@main.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        logger.debug(f"Received data for new user: {data}")
        
        # Check if shelter_id exists
        if data.get('shelter_id'):
            shelter = Shelter.query.get(data['shelter_id'])
            if not shelter:
                logger.debug(f"Shelter with id {data['shelter_id']} not found")
                return jsonify({'error': 'Shelter not found'}), 400
        
        new_user = User(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            shelter_id=data.get('shelter_id'),
            clinic_id=data.get('clinic_id')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'user': {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'shelter_id': new_user.shelter_id,
            'clinic_id': new_user.clinic_id,
            'created_at': new_user.created_at,
            'updated_at': new_user.updated_at
        }}), 201
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        logger.exception(e)
        return jsonify({'error': 'Internal Server Error'}), 500

# Маршрут для получения всех пользователей
@main.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.name for user in users]), 200
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        logger.exception(e)
        return jsonify({'error': 'Internal Server Error'}), 500

# Маршрут для создания приюта
@main.route('/shelters', methods=['POST'])
def create_shelter():
    try:
        data = request.get_json()
        logger.debug(f"Received data for new shelter: {data}")
        new_shelter = Shelter(
            name=data['name'],
            description=data.get('description'),
            location_id=data.get('location_id'),
            contact_info=data.get('contact_info')
        )
        db.session.add(new_shelter)
        db.session.commit()
        return jsonify({'message': 'Shelter created successfully'}), 201
    except Exception as e:
        logger.error(f"Error creating shelter: {e}")
        logger.exception(e)
        return jsonify({'error': 'Internal Server Error'}), 500

# Маршрут для получения всех приютов
@main.route('/shelters', methods=['GET'])
def get_shelters():
    try:
        shelters = Shelter.query.all()
        return jsonify([shelter.name for shelter in shelters]), 200
    except Exception as e:
        logger.error(f"Error fetching shelters: {e}")
        logger.exception(e)
        return jsonify({'error': 'Internal Server Error'}), 500