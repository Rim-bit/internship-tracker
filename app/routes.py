from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app.models import Application
from app.extensions import db


main_bp = Blueprint("main", __name__)

# Home page
@main_bp.route('/', methods=['POST', 'GET'])
def index():
    # Save info to database if valid
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
            return redirect(url_for("main.index"))
    else:
        internship_info = Application.query.order_by(Application.id).all()
        return render_template('index.html', internship_info=internship_info)


@main_bp.route('/delete/<int:application_id>', methods=['POST'])
def delete_row(application_id):
    application = Application.query.get(application_id)
    try:
        db.session.delete(application)
        db.session.commit()
        return redirect(url_for("main.index"))

    except:
        db.session.rollback()
        return redirect(url_for("main.index"))



