from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlalchemy as sa

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    # initialize flask app
    app = Flask(__name__)

    # add configuration from object
    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)

    from command.db import db_cmd
    app.register_blueprint(db_cmd)

    from controller import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    engine = sa.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sa.inspect(engine)
    if not inspector.has_table("users"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info('Initialized the database!')
    else:
        app.logger.info('Database already contains the users table.')


    return app
