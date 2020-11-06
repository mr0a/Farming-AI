from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config
from sqlalchemy import create_engine


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'my_flask_secret_app'
    app.config.from_object(Config)
    DB_URI = app.config['SQLALCHEMY_DATABASE_URI']
    engine = create_engine(DB_URI)
    #  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #  for sqlite db

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()
        return app

