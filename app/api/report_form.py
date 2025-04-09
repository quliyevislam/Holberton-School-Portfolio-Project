import logging
from flask import Blueprint, request, jsonify
from app.models import db, Report
import os

logger = logging.getLogger(__name__)

report_bp = Blueprint('report', __name__)

@report_bp.route('/submit_report', methods=['POST'])
def submit_report():
    logger.info("submit_report endpoint called")
    try:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        country_code = request.form.get('country_code')
        location = request.form.get('location')
        description = request.form.get('description')
        photo = request.files.get('photo')

        if not all([first_name, last_name, email, phone, location, description]):
            return jsonify({"error": "All fields are required"}), 400

        photo_url = None
        if photo:
            photo_filename = f"{first_name}_{last_name}_{photo.filename}"
            photo_path = os.path.join('static/uploads', photo_filename)
            photo.save(photo_path)
            photo_url = f"/{photo_path}"

        report = Report(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=f"{country_code}-{phone}",
            location=location,
            description=description,
            photo_url=photo_url
        )
        db.session.add(report)
        db.session.commit()

        return jsonify({"message": "Report submitted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
