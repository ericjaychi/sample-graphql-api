from .models import Book


# Returns all the Books from the database.
def get_books_resolver(obj, info):
	try:
		# Grabs all the books and puts them into a list of dictionaries.
		books = [book.serialize() for book in Book.query.all()]

		# Create a payload that will be sent back to the user when this is invoked.
		payload = {
			"success": True,
			"books": books
		}
	except Exception as error:
		# Create a payload that contains the thrown exception.
		payload = {
			"success": False,
			"errors": [str(error)]
		}
	return payload
