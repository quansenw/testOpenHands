# -*- coding: utf-8 -*-
"""
JWT Token 工具
"""

import jwt
import time
from functools import wraps
from flask import current_app, g, jsonify, request


def generate_token(user_id, phone):
    """生成访问令牌"""
    payload = {
        'user_id': user_id,
        'phone': phone,
        'exp': int(time.time()) + current_app.config['JWT_ACCESS_TOKEN_EXPIRES'],
        'iat': int(time.time())
    }
    return jwt.encode(payload, current_app.config['JWT_SECRET_KEY'], algorithm='HS256')


def verify_token(token):
    """验证令牌"""
    try:
        payload = jwt.decode(token, current_app.config['JWT_SECRET_KEY'], algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def token_required(f):
    """Token验证装饰器"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        # 从Header获取Token
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header[7:]
        
        if not token:
            return jsonify({'code': 401, 'message': '缺少访问令牌'}), 401
        
        payload = verify_token(token)
        if not payload:
            return jsonify({'code': 401, 'message': '令牌无效或已过期'}), 401
        
        # 将用户信息放入请求上下文
        g.user_id = payload.get('user_id')
        g.phone = payload.get('phone')
        
        return f(*args, **kwargs)
    
    return decorated


def get_current_user_id():
    """获取当前登录用户ID"""
    return getattr(g, 'user_id', None)


def get_current_phone():
    """获取当前登录手机号"""
    return getattr(g, 'phone', None)