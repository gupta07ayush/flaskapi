from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)

# Define some sample data
books = [
    {"id": 1, "title": "Python Programming", "author": "John Smith"},
    {"id": 2, "title": "Web Development with Flask", "author": "Jane Doe"}
]

# Define a route for the API endpoint
@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/")
def home():
    print("I am print statement")
    return "I am home.This is a docker image hosted on dockerhub Goto the endpoint /api/books"



# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
