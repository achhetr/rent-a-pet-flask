from flask import Flask


def create_app():
    # initialize flask app
    app = Flask(__name__)

    # add configuration from object
    app.config.from_object("config.app_config")

    return app
