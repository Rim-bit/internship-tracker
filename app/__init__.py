from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    # Home page
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return "About page!"

    return app
