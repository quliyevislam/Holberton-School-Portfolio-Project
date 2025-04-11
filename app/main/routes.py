from flask import render_template, request, redirect, url_for, flash, Flask, jsonify
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from app import login_manager
from app.main import bp as main
from app.models import db, User, Shelter
from app.CRUD.location import (
    create_new_location,
    get_location_by_id,
    update_location_by_id,
    delete_location_by_id,
    get_all_locations,
)
from app.CRUD.user import (
    create_new_user,
    get_user_by_id,
    update_user_by_id,
    delete_user_by_id,
    get_all_users,
    create_admin_user,
)
from app.CRUD.shelter_account import (
    create_new_shelter_account,
    get_all_shelter_accounts,
    get_shelter_account_by_id,
    update_shelter_account,
    delete_shelter_account_by_id,
)
from app.CRUD.animal_shelter import (
    create_animal,
    get_all_animals,
    get_animal_by_id,
    update_animal,
    delete_animal,
)
import logging
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from config import Config
# from google import genai
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)
# client = genai.Client(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route("/")
def index():
    return render_template("index.html")

@main.route("/welcome")
def welcome():
    return render_template("welcome.html")


@main.route("/report")
def report():
    return render_template("report.html")


@main.route("/map")
def map():
    google_map_key = os.environ.get("GOOGLE_MAPS_KEY")
    return render_template("map.html", google_map_key=google_map_key)


@main.route("/community")
def community():
    return render_template("community.html")


@main.route("/adopt")
def adopt():
    return render_template("adopt.html")


@main.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user exists
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Invalid email or password. Please try again.", "danger")
            return redirect(url_for("main.signin"))

        # Log the user in
        login_user(user)
        flash("Logged in successfully!", "success")
        return redirect(url_for("main.profile"))

    return render_template("signin.html")


@main.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        email = request.form.get("email")
        password = request.form.get("password")
        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "danger")
            return redirect(url_for("main.signup"))

        create_new_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        flash("Account created successfully!", "success")
        return redirect(url_for("main.signin"))

    return render_template("signup.html")


@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@main.route("/privacy")
def privacy():
    return render_template("privacy.html")


@main.route("/terms")
def terms():
    return render_template("terms.html")


@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.index"))
