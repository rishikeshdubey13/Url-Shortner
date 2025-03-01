from flask import Blueprint, redirect, jsonify, request
from app import db
from app.models import URL
import random, string

main = Blueprint('main', __name__)

def generate_random_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=7))
