from flask import Blueprint, redirect, jsonify, request
from app import db
from app.models import URL
import random, string

main = Blueprint('main', __name__)

def generate_random_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=7))

@main.route('/shorten', methods = ['POST'])
def shorten_url():
    data = request.json()
    long_url = data.get('url')

    if not long_url:
        return jsonify({'error': 'url is required'}), 400
    
    existing_url = URL.query.filter_by(long_url = long_url).first() 
    if existing_url:
        return jsonify({"short_url": f"http://127.0.0.1:5000/s/{existing_url.short_code}"})
    
    