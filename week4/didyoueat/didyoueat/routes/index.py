"""
home page
"""
from flask import Blueprint


HOME_API = Blueprint('home_API', __name__)

@HOME_API.route('/')
def home():
    """
    home page
    """
    return 'Hello, World!'
