# Flask Web Server Gateway Interface (application factory, handles configs.)
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# Initialize flask-SQLAlchemy data base.
db = SQLAlchemy()
DB_NAME = 'database.db'
# Application factory function.
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # Encryption. - TO DO
    app.config['SECRET_KEY'] = 'dev-temp' 
    # Telling Flask where the database is located. - READ MORE
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    if test_config is None:
        # Configs for live build.
        app.config.from_pyfile('config.py',silent=True)
    else:
        # Config for tests
        app.config.from_mapping(test_config)
    # Ensure intance folder exist.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Initialize Flask application for database.
    db.init_app(app)
    # import and register flask blueprints to application.
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # Imports models for SQLAlchemy to create database with.
    from .models import User
    from .models import Note
    with app.app_context():
        db.create_all()
    # Handles Login auth.
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    # Returns id of current user.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app
#