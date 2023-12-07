from flask import Flask, abort
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from qr_encoder.config import ProductionConfig

'''
    APP CONFIG
'''

csrf = CSRFProtect()
limiter = Limiter(
    get_remote_address,
    default_limits=["50 per day", "10 per hour"],
    storage_uri="memory://",
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    if not app.secret_key:
        raise ValueError("No SECRET_KEY set for Flask application")
        abort(500)

    csrf.init_app(app)
    limiter.init_app(app)

    from qr_encoder.main.routes import main
    app.register_blueprint(main)

    return app
