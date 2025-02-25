import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import User, Shelter, CatShelter
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

def populate_db():
    shelter = Shelter(name="Happy Tails Shelter", description="A shelter for cats and dogs", contact_info="123-456-7890")
    db.session.add(shelter)
    db.session.commit()

    user = User(name="John Doe", email="john@example.com", password=generate_password_hash("password", method='pbkdf2:sha256'), shelter_id=shelter.id)
    db.session.add(user)
    db.session.commit()

    cat1 = CatShelter(name="Whiskers", age=2, breed="Siamese", description="A playful cat", status="Available", shelter_id=shelter.id)
    cat2 = CatShelter(name="Mittens", age=3, breed="Tabby", description="A friendly cat", status="Adopted", shelter_id=shelter.id)
    db.session.add(cat1)
    db.session.add(cat2)
    db.session.commit()

    print("Database populated successfully!")

if __name__ == "__main__":
    populate_db()
