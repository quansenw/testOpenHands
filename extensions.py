# -*- coding: utf-8 -*-
"""
Flask extensions
Use a single db instance that will be initialized with app
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()