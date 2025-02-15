#!/usr/bin/python3
"""Defines the app_views Blueprint for API v1."""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
