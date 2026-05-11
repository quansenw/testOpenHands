# -*- coding: utf-8 -*-
"""
短信发送工具
生产环境需对接真实短信网关（阿里云、腾讯云等）
"""

import logging
from models.sms import SmsLog
from extensions import db

logger = logging.getLogger(__name__)


def send_sms(phone, scene='login'):
    """
    发送短信验证码
    
    Args:
        phone: 手机号
        scene: 场景 (login/bind_phone/reset_password)
    
    Returns:
        (success: bool, message: str)
    """
    # 验证手机号格式
    if not phone or len(phone) != 11 or not phone.startswith('1'):
        return False, '手机号格式不正确'
    
    # 检查发送频率
    if not SmsLog.can_send(phone):
        return False, f'发送过于频繁，请{SmsLog.SEND_INTERVAL}秒后重试'
    
    # 生成验证码
    code = SmsLog.generate_code()
    
    # TODO: 生产环境调用真实短信API发送
    # 示例：阿里云短信、腾讯云短信等
    # send_sms_via_gateway(phone, code, scene)
    
    # 模拟发送成功（开发环境直接打印）
    logger.info(f"[模拟发送短信] phone={phone}, code={code}, scene={scene}")
    
    # 记录到数据库
    sms_log = SmsLog(
        phone=phone,
        code=code,
        scene=scene
    )
    db.session.add(sms_log)
    db.session.commit()
    
    return True, '验证码已发送'


def verify_code(phone, code):
    """
    验证短信验证码
    
    Args:
        phone: 手机号
        code: 验证码
    
    Returns:
        (success: bool, message: str)
    """
    # 查找最新的有效验证码
    sms_log = SmsLog.query.filter_by(
        phone=phone, 
        scene='login'
    ).order_by(
        SmsLog.created_at.desc()
    ).first()
    
    if not sms_log:
        return False, '请先获取验证码'
    
    if not sms_log.is_valid():
        return False, '验证码已失效，请重新获取'
    
    if sms_log.code != code:
        return False, '验证码错误'
    
    # 标记为已使用
    sms_log.status = 1
    db.session.commit()
    
    return True, '验证成功'