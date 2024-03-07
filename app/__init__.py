from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='../templates')

    # Configure MySQL database
    app.config['SECRET_KEY'] = "6yamim1967"

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:6yamim1967@mysql/dbcard'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    with app.app_context():
        # Import and register blueprints here if you have any
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app


