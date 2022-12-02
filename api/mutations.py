from .models import Book
from api import db

from ariadne import convert_kwargs_to_snake_case


# Creates a new Book into the database.
@convert_kwargs_to_snake_case
def create_book_resolver(obj, info, title, author, isbn):
	try:
		# Creating a new Book object from the parameters from the user.
		new_book = Book(title=title, author=author, isbn=isbn)

		# Updating the database with the new Book object.
		db.session.add(new_book)
		db.session.commit()

		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"book": new_book.serialize()
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload