from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    # Home page
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return "About page!"

    return app
