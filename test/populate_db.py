import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User, Shelter, CatShelter, DogShelter, Location
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

def populate_db():
    shelter1 = Shelter(name="Happy Tails Shelter", description="A shelter for cats and dogs", contact_info="123-456-7890")
    shelter2 = Shelter(name="Paws and Claws", description="A shelter for all pets", contact_info="987-654-3210")
    shelter3 = Shelter(name="Furry Friends", description="A shelter for furry friends", contact_info="555-555-5555")
    db.session.add_all([shelter1, shelter2, shelter3])
    db.session.commit()

    def add_user_if_not_exists(name, email, password, shelter_id):
        if not User.query.filter_by(email=email).first():
            user = User(name=name, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'), shelter_id=shelter_id)
            db.session.add(user)
            db.session.commit()

    add_user_if_not_exists("John Doe", "john@example.com", "password", shelter1.id)
    add_user_if_not_exists("Jane Smith", "jane@example.com", "password", shelter2.id)
    add_user_if_not_exists("Alice Johnson", "alice@example.com", "password", shelter3.id)

    location1 = Location(name="Downtown", description="Central city area", info="Near the main square")
    location2 = Location(name="Suburbs", description="Residential area", info="Quiet and peaceful")
    location3 = Location(name="Countryside", description="Rural area", info="Surrounded by nature")
    db.session.add_all([location1, location2, location3])
    db.session.commit()

    cat1 = CatShelter(name="Whiskers", age=2, breed="Siamese", description="A playful cat", status="Available", shelter_id=shelter1.id)
    cat2 = CatShelter(name="Mittens", age=3, breed="Tabby", description="A friendly cat", status="Adopted", shelter_id=shelter2.id)
    cat3 = CatShelter(name="Shadow", age=4, breed="Persian", description="A calm cat", status="Available", shelter_id=shelter3.id)
    db.session.add_all([cat1, cat2, cat3])
    db.session.commit()

    dog1 = DogShelter(name="Buddy", age=3, breed="Labrador", description="A loyal dog", status="Available", shelter_id=shelter1.id)
    dog2 = DogShelter(name="Max", age=5, breed="German Shepherd", description="A protective dog", status="Adopted", shelter_id=shelter2.id)
    dog3 = DogShelter(name="Bella", age=2, breed="Golden Retriever", description="A friendly dog", status="Available", shelter_id=shelter3.id)
    db.session.add_all([dog1, dog2, dog3])
    db.session.commit()

    print("Database populated successfully!")

if __name__ == "__main__":
    populate_db()
