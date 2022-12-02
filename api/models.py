from api import db


# Define a class that will represent the model.
class Book(db.Model):
	# Defining the columns inside the database.
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	author = db.Column(db.String)
	isbn = db.Column(db.String)

	# Method that translates the data into a JSON / Dictionary.
	def serialize(self):
		return {
			"id": self.id,
			"title": self.title,
			"author": self.author,
			"isbn": self.isbn
		}
