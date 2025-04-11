from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user
from werkzeug.security import check_password_hash
from app.models import User
from app.CRUD.user import create_new_user
from app.api import bp

@bp.route("/signin", methods=["GET", "POST"])
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


@bp.route("/signup", methods=["GET", "POST"])
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