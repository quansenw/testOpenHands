# -*- coding: utf-8 -*-
"""
Auth API Routes
用户认证模块：发送验证码、登录/注册
"""

from flask import Blueprint, request, jsonify
from datetime import datetime

from extensions import db
from models import User, CommonUser, UserLogin
from utils.token import generate_token
from utils.sms import send_sms, verify_code

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/send_code', methods=['POST'])
def send_code():
    """
    发送短信验证码
    POST /api/auth/send_code
    {
        "phone": "13800138000",
        "scene": "login"  # 可选，默认login
    }
    """
    data = request.get_json() or {}
    phone = data.get('phone', '').strip()
    scene = data.get('scene', 'login')
    
    # 参数校验
    if not phone:
        return jsonify({'code': 400, 'message': '手机号不能为空'}), 400
    
    if len(phone) != 11:
        return jsonify({'code': 400, 'message': '手机号格式不正确'}), 400
    
    # 发送验证码
    success, message = send_sms(phone, scene)
    
    if not success:
        return jsonify({'code': 400, 'message': message}), 400
    
    return jsonify({
        'code': 200, 
        'message': '验证码已发送',
        'data': {
            'expire': 300  # 5分钟有效期
        }
    })


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    验证码登录（即注册）
    POST /api/auth/login
    {
        "phone": "13800138000",
        "code": "123456"
    }
    """
    data = request.get_json() or {}
    phone = data.get('phone', '').strip()
    code = data.get('code', '').strip()
    
    # 参数校验
    if not phone:
        return jsonify({'code': 400, 'message': '手机号不能为空'}), 400
    
    if not code:
        return jsonify({'code': 400, 'message': '验证码不能为空'}), 400
    
    # 验证验证码
    success, message = verify_code(phone, code)
    
    if not success:
        return jsonify({'code': 400, 'message': message}), 400
    
    # 登录即注册：查找用户或创建新用户
    user = User.query.filter_by(phone=phone).first()
    
    if not user:
        # 新用户注册
        user = User(
            username=f"user_{phone[-4:]}_{datetime.now().timestamp()}",
            phone=phone,
            nickname=f"用户{phone[-4:]}"
        )
        db.session.add(user)
        db.session.flush()
        
        # 创建 common_user 记录
        common_user = CommonUser(uid=user.id)
        db.session.add(common_user)
    
    # 更新最近登录时间
    common_user = CommonUser.query.get(user.id)
    if common_user:
        common_user.last_login_at = int(datetime.now().timestamp())
    
    # 记录登录历史
    login_record = UserLogin(
        user_id=user.id,
        device=request.headers.get('User-Agent', ''),
        ip=request.remote_addr
    )
    db.session.add(login_record)
    db.session.commit()
    
    # 生成Token
    token = generate_token(user.id, user.phone)
    
    return jsonify({
        'code': 200,
        'message': '登录成功',
        'data': {
            'token': token,
            'user': user.to_dict()
        }
    })


@auth_bp.route('/profile', methods=['GET'])
def get_profile():
    """
    获取用户信息（需登录）
    GET /api/auth/profile
    Headers: Authorization: Bearer <token>
    """
    from flask import g
    from utils.token import token_required, get_current_user_id
    
    # Apply token_required manually
    from utils.token import verify_token
    
    token = None
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header[7:]
    
    if not token:
        return jsonify({'code': 401, 'message': '缺少访问令牌'}), 401
    
    from utils.token import verify_token
    payload = verify_token(token)
    if not payload:
        return jsonify({'code': 401, 'message': '令牌无效或已过期'}), 401
    
    user_id = payload.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404
    
    return jsonify({
        'code': 200,
        'message': 'success',
        'data': user.to_dict()
    })


@auth_bp.route('/refresh_token', methods=['POST'])
def refresh_token():
    """
    刷新Token
    POST /api/auth/refresh_token
    Headers: Authorization: Bearer <token>
    """
    from utils.token import verify_token, generate_token
    
    token = None
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header[7:]
    
    if not token:
        return jsonify({'code': 401, 'message': '缺少访问令牌'}), 401
    
    payload = verify_token(token)
    if not payload:
        return jsonify({'code': 401, 'message': '令牌无效或已过期'}), 401
    
    user_id = payload.get('user_id')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'code': 404, 'message': '用户不存在'}), 404
    
    new_token = generate_token(user.id, user.phone)
    
    return jsonify({
        'code': 200,
        'message': 'Token已刷新',
        'data': {
            'token': new_token
        }
    })