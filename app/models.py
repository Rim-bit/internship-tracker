from app import db
from datetime import datetime, UTC
# model = blueprint for database
class Application(db.Model):
    # primary_key means each row gets unique identifier
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=True)

    # Return a readable string representation of one Application row
    def __repr__(self):
        return '<Application %r>' % self.id
