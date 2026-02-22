from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import config_options

bcrypt = Bcrypt()
jwt = JWTManager()
db = SQLAlchemy()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])

    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)

    return app


from app.api.v1.users import user_bp
from app.api.v1.auth import auth_bp

app.register_blueprint(user_bp, url_prefix='/api/v1/users')
app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')