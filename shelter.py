# @main.route('/admin')
# @jwt_required()
# def admin():
#     current_user_id = get_jwt_identity()
#     user = get_user_by_id(current_user_id)
#     return render_template('admin/admin.html', user=user)
#
# @main.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         data = request.get_json()
#         email = data.get('email')
#         password = data.get('password')

#         app.logger.debug(f"Login attempt with email: {email}")

#         if email == 'admin@admin' and password == 'admin':
#             access_token = create_access_token(identity='admin')
#             flash('Logged in as admin successfully!', 'success')
#             response = jsonify(access_token=access_token)
#             response.status_code = 200
#             response.headers['Location'] = url_for('main.admin')
#             return response

#         user = User.query.filter_by(email=email).first()

#         if user and check_password_hash(user.password, password):
#             access_token = create_access_token(identity=user.id)
#             flash('Logged in successfully!', 'success')
#             response = jsonify(access_token=access_token)
#             response.status_code = 200
#             response.headers['Location'] = url_for('main.home')
#             return response
#         else:
#             app.logger.debug(f"Login failed for email: {email}")
#             flash('Login failed. Check your email and password.', 'danger')
#             return jsonify({"msg": "Login failed. Check your email and password."}), 401

#     return render_template('auth/login.html')

# @main.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         try:
#             data = request.get_json()
#             name = data.get('name')
#             email = data.get('email')
#             password = data.get('password')
#             confirm_password = data.get('confirm_password')

#             if password != confirm_password:
#                 flash('Passwords do not match!', 'danger')
#                 return jsonify({"msg": "Passwords do not match!"}), 400

#             hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
#             new_user = User(name=name, email=email, password=hashed_password)
#             db.session.add(new_user)
#             db.session.commit()

#             flash('Account created successfully!', 'success')
#             return jsonify({"msg": "Account created successfully!"}), 201
#         except Exception as e:
#             app.logger.error(f"Error creating user: {e}")
#             return jsonify({"msg": "Internal server error"}), 500

#     return render_template('auth/sign_up.html')

