from app import db

class URL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    short_code = db.Column(db.String(7), unique = True, nullable = False)
    long_url = db.Column(db.String(2048), nullable = False)
    

    
