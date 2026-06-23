from flask import Flask, render_template, request, redirect
from config import Config
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register the routes blueprint after the app is created to avoid circular import issues
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
