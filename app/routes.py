from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Application
from app.extensions import db


main_bp = Blueprint("main", __name__)

# Home page
@main_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        company_name = request.form['company']
        company_data = Application(company=company_name)

        try:
            db.session.add(company_data)
            db.session.commit()
            return redirect(url_for("main.index"))
        except:
            return "There was an issue adding company name"
    else:
        return render_template('index.html')

@main_bp.route('/about')
def about():
    return "About page!"
