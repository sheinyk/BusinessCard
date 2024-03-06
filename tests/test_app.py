# # tests/test_app.py
#
# import unittest
# from flask_testing import TestCase
# from app.app import create_app
#
#
# class TestApp(TestCase):
#
#     def create_app(self):
#         return create_app(config_name='test')
#         # self.client = self.app.test_client()
#
#     def setUp(self):
#         # Set up the Flask test client
#         self.client = self.app.test_client()
#
#     def test_home_page(self):
#         # Test the home page without accessing the database
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'', response.data)
#
#
# if __name__ == '__main__':
#     unittest.main()

#
# from app import create_app
#
# app = create_app(config_name='test')
#
#
# def test_home_page(self):
#     # Test the home page without accessing the database
#     response = self.app.get('/')
#     self.assertEqual(response.status_code, 200)
#     self.assertIn(b'submit', response.data)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# import sqlite3
# import unittest
# from flask_sqlalchemy import SQLAlchemy
# from app.app import create_app
#
#
# class TestConfig:
#     DATABASE_URI = "sqlite:///test_database.db"
#
#
# class DatabaseHelper:
#     @staticmethod
#     def connect(database_uri):
#         return sqlite3.connect(database_uri)
#
#
# def create_table(cursor):
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, firstName TEXT, lastName TEXT, phoneNumber TEXT, email TEXT, message TEXT)")
#
#
# def insert_data(cursor, data):
#     insert_query = "INSERT INTO card (firstName, lastName, phoneNumber, email, message) VALUES (?, ?, ?, ?, ?)"
#     cursor.execute(insert_query, data)
#
#
# def fetch_data(cursor):
#     cursor.execute("SELECT * FROM card")
#     return cursor.fetchall()
#
#
# class TestDatabase(unittest.TestCase):
#     def setUp(self):
#         app = create_app(TestConfig)
#         self.db = SQLAlchemy(app)
#         self.connection = self.db.engine.connect()
#
#     def tearDown(self):
#         self.connection.close()
#         self.db.session.remove()
#         self.db.drop_all()
#
#     def test_database_operations(self):
#         cursor = self.connection
#         create_table(cursor)
#         data = ('John', 'Doe', '123456789', 'john.doe@example.com', 'Test message')
#         insert_data(cursor, data)
#         result = fetch_data(cursor)
#         self.assertEqual(len(result), 1)
#         self.assertEqual(result[0]['firstName'], 'John')
#
#
# if __name__ == '__main__':
#     unittest.main()
