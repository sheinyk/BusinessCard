from flask import Flask, render_template, request, redirect, url_for, Blueprint
from app.app import YourForm
from app.models import Card
from . import db

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    your_form = YourForm()

    if request.method == 'POST' and your_form.validate_on_submit():
        # Extract form data using WTForms
        firstName = your_form.firstName.data
        lastName = your_form.lastName.data
        phoneNumber = your_form.phoneNumber.data
        email = your_form.email.data
        message = your_form.message.data

        # Create a Card instance and add it to the database
        card = Card(firstName=firstName, lastName=lastName, phoneNumber=phoneNumber, email=email, message=message)
        db.session.add(card)
        db.session.commit()

        return render_template('error.html', firstName=firstName)

    return render_template('BCard.html', form=your_form, success_message='Form submitted successfully')


# # Error page route
# @main.route('/error_page/<string:firstName>')
# def error_page(firstName):
#     # Your error page logic here
#     return render_template('error.html', firstName=firstName)

# if __name__ == '__main__':
#     db.create_all()  # Create tables before running the app
#     main.run(debug=True)
