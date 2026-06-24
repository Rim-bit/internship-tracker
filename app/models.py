from app.extensions import db

class Application(db.Model):
    # primary_key means each row gets unique identifier
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(200), nullable=True)
    status = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200), nullable=True)
    applied_date = db.Column(db.String(200), nullable=True)
    deadline = db.Column(db.String(200), nullable=True)
    link = db.Column(db.String(200), nullable=True)

    # Return a readable string representation of one Application row
    def __repr__(self):
        return '<Application %r>' % self.id
  