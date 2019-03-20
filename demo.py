#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello zappa!", 200

@app.route('/hello/<name>')
@app.route('/hello/')
def custom_hello(name=None):
    if name is None:
        return "Tell me your name", 200
    else:
        return "Hello " + name + "!", 200

# We only need this for local development.
if __name__ == '__main__':
    app.run()