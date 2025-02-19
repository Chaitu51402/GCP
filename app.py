from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Simple Flask application to test in production Part3'