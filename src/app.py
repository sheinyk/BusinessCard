from flask_wtf import FlaskForm
import mysql.connector
from flask import Flask, render_template, request, redirect, url_for
from wtforms.fields.simple import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '6yamim1967'
db = mysql.connector.connect(
    host='mysql',
    user='root',
    password='6yamim1967',
    database='dbcard'
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS card (id INT AUTO_INCREMENT PRIMARY KEY, "
               "firstName VARCHAR(20) NOT NULL, "
               "lastName VARCHAR(20), phoneNumber VARCHAR(20) NOT NULL, "
               "email VARCHAR(50), message VARCHAR(500))")
db.commit()


class YourForm(FlaskForm):
    firstName = StringField('שם פרטי')
    lastName = StringField('שם משפחה')
    phoneNumber = StringField('מספר טלפון')
    email = StringField('כתובת מייל')
    message = StringField('מוזמנים לכתוב לנו')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract form data
            firstName = request.form.get('firstName', ' ')
            lastName = request.form.get('lastName', ' ')
            phoneNumber = request.form['phoneNumber']
            email = request.form.get('email', ' ')
            message = request.form.get('message', ' ')

            # Insert data into the Card table
            insert_query = "INSERT INTO card (firstName, lastName, phoneNumber, email, message) " \
                           "VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (firstName, lastName, phoneNumber, email, message))
            db.commit()

            return redirect(url_for('success'))  # Redirect to a success route
        except Exception:
            firstName = request.form.get('firstName', '')

            return render_template('error.html', firstName=firstName)
    else:

        your_form = YourForm()

        return render_template('BCard.html', form=your_form)
