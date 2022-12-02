from api import app, db

from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, \
	ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import get_books_resolver
from api.mutations import create_book_resolver

# Defines the execution type that wishes to be done. In this case we defined a Query type inside schema.graphql.
# This will allow us to tie a resolver to a method within the schema.graphql file.
query = ObjectType("Query")

# Allows us to use the functions under the Mutation type that is defined inside of schema.graphql.
mutation = ObjectType("Mutation")

# Binds the keyword that users will invoke to the respective function that is defined from the API perspective.
query.set_field("getBooks", get_books_resolver)

mutation.set_field("createBook", create_book_resolver)

# Loads the path to the schema file. Since it's in the same directory, we can simply just input the name.
type_defs = load_schema_from_path("/Users/eric-chi/Dropbox/__igor/repos/blogs/sample-graphql-api/schema.graphql")

# Takes all the information we defined and allows it to be executed when invoked.
schema = make_executable_schema(
	type_defs, query, mutation, snake_case_fallback_resolvers
)


# Enables a GET endpoint for Flask under the "/graphql" route.
@app.route("/graphql", methods=["GET"])
def graphql_playground():
	# Returns the UI for the Playground when "/graphql" is hit within your application.
	return PLAYGROUND_HTML, 200


# Enables a POST endpoint for Flask under the "/graphql" route.
@app.route("/graphql", methods=["POST"])
def graphql_server():
	# Pull the data from the POST request that was made to the server.
	data = request.get_json()

	# This executes the query against the schema that we defined.
	success, result = graphql_sync(
		schema,
		data,
		context_value=request,
		debug=app.debug
	)

	# Checks to see if the
	if success:
		status_code = 200
	else:
		status_code = 400

	# Returns the response back to the user dependent.
	return jsonify(result), status_code


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
	# Runs the Flask application only if the main.py file is being run.
	app.run()
