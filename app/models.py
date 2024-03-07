from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from . import db


class Card(db.Model):
    __tablename__ = 'card'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255), nullable=False)
    lastName = db.Column(db.String(255), nullable=False)
    phoneNumber = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    message = db.Column(db.Text, nullable=True)


class YourForm(FlaskForm):
    firstName = StringField('שם פרטי')
    lastName = StringField('שם משפחה')
    phoneNumber = StringField('מספר טלפון')
    email = StringField('כתובת מייל')
    message = StringField('מוזמנים לכתוב לנו')
    submit = SubmitField('Submit')
