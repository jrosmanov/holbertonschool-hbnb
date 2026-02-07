#!/usr/bin/python3
from flask import Flask
from flask_restx import Api
from hbnb.api.v1.users import api as users_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, title="HBnB API", version="1.0")
    api.add_namespace(users_ns, path="/api/v1/users")
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
