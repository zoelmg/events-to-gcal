from .db import db

class Users(db.Model):
    nickname = db.Column(db.String(20), primary_key=True)
    real_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), nullable=True)


