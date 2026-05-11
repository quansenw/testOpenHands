# -*- coding: utf-8 -*-
"""
北海365分类信息系统 - 用户模块
包含：登录、注册、短信验证码
"""

from flask import Flask
from config import config
from dotenv import load_dotenv

load_dotenv()

# This must be imported after extensions.py defines db
from extensions import db


def create_app(config_name='development'):
    """Application factory."""
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config[config_name])
    
    # Initialize db with app
    db.init_app(app)
    
    # Register blueprints
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app


# Run the application
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)