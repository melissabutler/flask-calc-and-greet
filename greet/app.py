from flask import Flask

from flask_debug import Debug

app = Flask(__name__)

@app.route('/')
def root_page():
    return """
    <html>
    <body>
        <h1>Home Page</h1>
        <p>Welcome to my app</p>
        <a href="/welcome">Go to welcome page</a>
    </body>
    </html>
    """

@app.route('/welcome')
def welcome_page():
    return "Welcome"

@app.route('/welcome/home')
def welcome_home_page():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back_page():
    return "Welcome back"