from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from flask import Flask, render_template, request, redirect, url_for

import mysql.connector


#
# app = Flask(__name__, template_folder='../templates')
# app.config['SECRET_KEY'] = '6yamim1967'
#
# db = mysql.connector.connect(
#     host='mysql',
#     user='root',
#     password='6yamim1967',
#     database='dbcard'
# )
#
# cursor = db.cursor()
#
# cursor.execute("CREATE TABLE IF NOT EXISTS card (id INT AUTO_INCREMENT PRIMARY KEY, "
#                "firstName VARCHAR(20) NOT NULL, "
#                "lastName VARCHAR(20), phoneNumber VARCHAR(20) NOT NULL, "
#                "email VARCHAR(50), message VARCHAR(500))")
# db.commit()
#

class YourForm(FlaskForm):
    firstName = StringField('שם פרטי')
    lastName = StringField('שם משפחה')
    phoneNumber = StringField('מספר טלפון')
    email = StringField('כתובת מייל')
    message = StringField('מוזמנים לכתוב לנו')
    submit = SubmitField('Submit')

#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     your_form = YourForm()
#
#     if request.method == 'POST' and your_form.validate_on_submit():
#         # Extract form data using WTForms
#         firstName = your_form.firstName.data
#         lastName = your_form.lastName.data
#         phoneNumber = your_form.phoneNumber.data
#         email = your_form.email.data
#         message = your_form.message.data
#
#         # Insert data into the Card table
#         insert_query = "INSERT INTO card (firstName, lastName, phoneNumber, email, message) " \
#                        "VALUES (%s, %s, %s, %s, %s)"
#         cursor.execute(insert_query, (firstName, lastName, phoneNumber, email, message))
#         db.commit()
#         return redirect(url_for('error_page', firstName=firstName))
#     return render_template('BCard.html', form=your_form, success_message='Form submitted successfully')
#
#
# @app.route('/error_page/<firstName>')
# def error_page(firstName):
#     # Render the error page with the provided data
#     return render_template('error.html', firstName=firstName)
# You can redirect to another page or render the same page with a success message
#     return render_template('BCard.html', form=your_form, success_message='Form submitted successfully')
# firstName=your_form.firstName.data
# return render_template('error.html', firstName=firstName)
