import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://user1:password@localhost:5432/url_shortner"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")  # Replace with a strong secret

