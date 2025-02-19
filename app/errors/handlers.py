from flask import render_template
import logging
from app.errors import bp

logger = logging.getLogger(__name__)

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.errorhandler(500)
def internal_error(error):
    logger.error(f"500 Internal Server Error: {error}")
    return render_template('errors/500.html'), 500