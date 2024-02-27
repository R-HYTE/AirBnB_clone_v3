#!/usr/bin/python3
"""Module defining API views for the index endpoint."""

from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage

# Define the classes dictionary
classes = {
        "amenities": Amenity,
        "cities": City,
        "places": Place,
        "reviews": Review,
        "states": State,
        "users": User,
}

@app_views.route('/status')
def status():
    """Return the API status"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats')
def stats():
    """Retrieves the number of each object by type"""
    stats = {}

    for key, value in classes.items():
        stats[key] = storage.count(value)

    return jsonify(stats)
