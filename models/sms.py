# -*- coding: utf-8 -*-
"""
短信验证码模型（s_sms_logs）
"""

import random
from datetime import datetime
from extensions import db


class SmsLog(db.Model):
    """短信验证码日志（s_sms_logs）"""
    __tablename__ = 's_sms_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    code = db.Column(db.String(8), nullable=False)
    scene = db.Column(db.String(32))  # 场景：login, register, bind_phone 等
    status = db.Column(db.SmallInteger, default=0)  # 0未使用 1已使用
    created_at = db.Column(db.Integer, default=lambda: int(datetime.now().timestamp()))
    
    # 验证码有效期（秒）
    CODE_EXPIRE = 300  # 5分钟
    
    # 发送间隔（秒）
    SEND_INTERVAL = 60  # 60秒
    
    @staticmethod
    def generate_code():
        """生成6位验证码"""
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    @staticmethod
    def can_send(phone):
        """检查是否可以发送验证码"""
        now = int(datetime.now().timestamp())
        # 查找最近的一条记录
        latest = SmsLog.query.filter_by(phone=phone).order_by(SmsLog.created_at.desc()).first()
        if latest and now - latest.created_at < SmsLog.SEND_INTERVAL:
            return False
        return True
    
    def is_valid(self):
        """验证码是否有效"""
        now = int(datetime.now().timestamp())
        return self.status == 0 and now - self.created_at < self.CODE_EXPIRE
    
    def to_dict(self):
        return {
            'id': self.id,
            'phone': self.phone,
            'scene': self.scene,
            'status': self.status,
            'created_at': self.created_at
        }