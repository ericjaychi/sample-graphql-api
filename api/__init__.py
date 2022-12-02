import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)

# Configuring a database for the Flask application defined above.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.getcwd()}/book.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Annotation that allows for the endpoints / URL to be hit.
@app.route('/')
def hello_world():
	return 'Hello World!'
