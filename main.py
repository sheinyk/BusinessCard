# from app import create_app
# app = create_app()
from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
# This module contains the main functionality of your application.
