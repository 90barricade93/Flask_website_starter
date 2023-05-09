# this is the main file that will run the flask app
# here we define the routes and the view functions
# we also import the render_template function from flask
# to render the html templates

from flask import Flask, render_template   # We imported render_template

app = Flask(__name__)  # We created a Flask instance called app

@app.route("/") # We created a route decorator
def home(): # We created a view function
    return render_template("home.html") # We returned a string
    
@app.route("/about") # We created a route decorator
def about(): # We created a view function
    return render_template("about.html") # We returned a string
    
if __name__ == "__main__": # We used this to run the Flask application only if the script is directly executed from the Python interpreter and not used as an imported module
    app.run(debug=True) # We ran the Flask app in debug mode
    