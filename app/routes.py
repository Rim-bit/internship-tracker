from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Application
from app.extensions import db


main_bp = Blueprint("main", __name__)

# Home page
@main_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        company = request.form.get('company', '').strip()
        role = request.form.get('role', '').strip()
        status = request.form.get('status', '').strip()
        location = request.form.get('location', '').strip()
        applied_date = request.form.get('applied_date', '').strip()
        deadline = request.form.get('deadline', '').strip()
        link = request.form.get('link', '').strip()
            
        if not company or not status:
            return redirect(url_for("main.index"))
        
        new_application = Application(
            company = company,
            role = role,
            status = status,
            location = location,
            applied_date = applied_date,
            deadline = deadline,
            link = link
        )

        try:
            db.session.add(new_application)
            db.session.commit()
            return redirect(url_for("main.index"))
        except:
            db.session.rollback()
            return "There was an issue adding company name"
    else:
        internship_info = Application.query.order_by(Application.id).all()
        return render_template('index.html', internship_info=internship_info)

@main_bp.route('/about')
def about():
    return "About page!"


