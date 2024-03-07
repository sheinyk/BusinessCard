from flask_sqlalchemy import SQLAlchemy

from . import db


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    phoneNumber = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=True)
