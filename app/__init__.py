from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager




db= SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS inside the app


    db.init_app(app)    
    jwt.init_app(app)
    migrate = Migrate(app, db)


    from app.routes import main
    from app.auth_routes import auth
    app.register_blueprint(main)
    app.register_blueprint(auth,url_prefix= '/auth')

    return app


