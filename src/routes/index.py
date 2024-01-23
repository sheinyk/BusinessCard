import flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from src.app import app
import os
from flask import Flask, render_template, request, redirect, url_for
from wtforms.fields.simple import StringField, SubmitField
from werkzeug.urls import url_encode as original_url_encode

app.config['SECRET_KEY'] = '6yamim1967'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'.format(
    username=os.getenv('DB_USERNAME', 'root'),
    password=os.getenv('DB_PASSWORD', '6yamim1967'),
    host=os.getenv('DB_HOST', 'localhost'),
    port=os.getenv('DB_PORT', '3306'),
    database=os.getenv('DB_NAME', 'dbcard')
)

db = SQLAlchemy(app)


class YourForm(FlaskForm):
    firstName = StringField('שם פרטי')
    lastName = StringField('שם משפחה')
    phoneNumber = StringField('מספר טלפון')
    email = StringField('כתובת מייל')
    message = StringField('מוזמנים לכתוב לנו')
    submit = SubmitField('Submit')


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20))
    phoneNumber = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50))
    message = db.Column(db.String(500))


@app.before_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def add():
    # global firstName
    if request.method == 'POST':
        try:
            # Extract form data
            firstName = request.form.get('firstName', '')
            lastName = request.form.get('lastName', '')
            phoneNumber = request.form['phoneNumber']
            email = request.form.get('email', '')
            message = request.form.get('message', '')

            # Create a new Card instance
            new_client = Card(firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, email=email,
                              message=message)

            # Add to the database
            db.session.add(new_client)
            db.session.commit()

            return redirect(url_for('success'))  # Redirect to a success route
        except Exception as e:
            # Handle errors (e.g., log the error)
            return render_template('error.html', firstName=firstName)
    else:
        # Create an instance of your form
        your_form = YourForm()

        # Render the template and pass the form to it
        return render_template('test.html', form=your_form)
