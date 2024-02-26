#!/usr/bin/python3
"""Module defining API views for the index endpoint."""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    '''Return the API status'''
    return jsonify({'status': 'OK'})
