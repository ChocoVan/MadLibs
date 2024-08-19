# create app and database functions here
# every route must be registered into this file as a blueprint
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = "fuck_my_life"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:man-mylife-is-2-4ked@localhost/cards'
    #app.config['SECRET KEY'] = 'fuck_my_life'
    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # flask db init
    # flask db
    # flask db migrate -m 'name of migration file'
    # flask db upgrade
    migrate = Migrate(app, db)

    from .routes import routes
    from .createPost import create
    from .game import game
    from .readPost import readPost

    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(create, url_prefix="/")
    app.register_blueprint(game, url_prefix="/")
    app.register_blueprint(readPost, url_prefix="/")

    from .database import Post

    with app.app_context():
        db.create_all()

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')