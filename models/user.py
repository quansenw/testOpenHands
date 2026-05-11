# -*- coding: utf-8 -*-
"""
用户模块数据库模型
根据 er-diagram.md 中用户域定义
"""

import uuid
import hashlib
from datetime import datetime
from extensions import db


class User(db.Model):
    """用户主表（s_user）"""
    __tablename__ = 's_user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    nickname = db.Column(db.String(128))
    phone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128))  # 密码哈希
    icon = db.Column(db.String(255))  # 头像
    is_delete = db.Column(db.SmallInteger, default=0)  # 0正常 1已删
    is_secrecy = db.Column(db.SmallInteger, default=0)  # 是否保密
    created_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()))
    
    # Relationships
    common_user = db.relationship('CommonUser', backref='user', uselist=False)
    logins = db.relationship('UserLogin', backref='user', lazy='dynamic')
    infos = db.relationship('FenleiInfo', backref='user', lazy='dynamic')
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'nickname': self.nickname,
            'phone': self.phone,
            'icon': self.icon,
            'created_at': self.created_at
        }
    
    def set_password(self, password):
        """设置密码"""
        if password:
            self.password = hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        """验证密码"""
        return self.password == hashlib.sha256(password.encode()).hexdigest() if self.password else False
    
    def generate_username(self):
        """生成唯一用户名"""
        return f"user_{self.phone[-4:]}_{uuid.uuid4().hex[:6]}"


class CommonUser(db.Model):
    """账号辅助表（common_user）- 1:1 关联"""
    __tablename__ = 'common_user'
    
    uid = db.Column(db.Integer, db.ForeignKey('s_user.id'), primary_key=True)
    status = db.Column(db.SmallInteger, default=1)  # 账号状态
    last_login_at = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'uid': self.uid,
            'status': self.status,
            'last_login_at': self.last_login_at
        }


class UserLogin(db.Model):
    """登录历史（s_user_login）"""
    __tablename__ = 's_user_login'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('s_user.id'), nullable=False)
    device = db.Column(db.String(64))  # 设备信息
    ip = db.Column(db.String(32))  # IP地址
    login_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()))
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'device': self.device,
            'ip': self.ip,
            'login_at': self.login_at
        }


class Forbid(db.Model):
    """封禁记录（s_forbid）"""
    __tablename__ = 's_forbid'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('s_user.id'), nullable=False)
    type = db.Column(db.SmallInteger)  # 封禁类型
    expire_at = db.Column(db.Integer)  # 过期时间戳
    reason = db.Column(db.String(255))
    
    def is_active(self):
        """是否在封禁中"""
        if self.expire_at:
            return self.expire_at > datetime.now().timestamp()
        return True  # 无过期时间则为永久封禁


class BindMobileRecord(db.Model):
    """换绑手机号历史（s_bindmobile_record）"""
    __tablename__ = 's_bindmobile_record'
    
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey('s_user.id'), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()))


class FenleiInfo(db.Model):
    """信息主表（s_fenlei_info）- 预留"""
    __tablename__ = 's_fenlei_info'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('s_user.id'))