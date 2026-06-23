from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Application
from app.extensions import db


main_bp = Blueprint("main", __name__)

# Home page
@main_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        new_application = Application(
            company = request.form['company'],
            role = request.form['role'],
            status = request.form['status'],
            location = request.form['location'],
            applied_date = request.form['applied_date'],
            deadline = request.form['deadline'],
            link = request.form['link']
        )
        try:
            db.session.add(new_application)
            db.session.commit()
            return redirect(url_for("main.index"))
        except:
            return "There was an issue adding company name"
    else:
        internship_info = Application.query.order_by(Application.id).all()
        return render_template('index.html', internship_info=internship_info)

@main_bp.route('/about')
def about():
    return "About page!"


