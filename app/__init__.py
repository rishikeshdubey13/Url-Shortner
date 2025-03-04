from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS




db= SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS inside the app


    db.init_app(app)
    migrate = Migrate(app, db)

    from app.routes import main
    app.register_blueprint(main)

    return app


