from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from api.routes.hello_world_routes import hello_world_routes
from api.routes.farcaster_routes import farcaster_routes
from os import path
# from api.models import *


db = SQLAlchemy()
DB_NAME = "dev.db"


def create_app():
    app = Flask(__name__)
    # SQLite database file
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    # engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


    app.register_blueprint(farcaster_routes, url_prefix="/api/farcaster")
    app.register_blueprint(hello_world_routes, url_prefix="/api/hello")

    from api.models.channel_models import Channel, User
    create_database(app)

    print("CLASS", Channel)

    return app


def create_database(app):
    if not path.exists("api/instance/" + DB_NAME):
        with app.app_context():
            db.create_all()  # Create all tables defined in models
            print("Database created successfully")
        print("Database created")



# if __name__ == "__main__":
#     app.run(debug=True)
