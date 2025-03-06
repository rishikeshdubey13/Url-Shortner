import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://user1:password@localhost:5432/url_shortner"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "3b2e3ef644b8d82213fe45730c2a89e1153cf8346d991d2efa446a9c45878d54")  # Replace with a strong secret

