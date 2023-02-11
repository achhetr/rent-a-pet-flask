from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # initialize flask app
    app = Flask(__name__)

    # add configuration from object
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)

    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app
