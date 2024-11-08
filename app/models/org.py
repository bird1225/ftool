# -*- coding: utf-8 -*-
# @Author  : 汪凌峰(Lingfeng Wang)
# @Date    : 2024/11/8 17:12
# models.py
from sqlalchemy import Column, String, Integer, DateTime, Text
from app.db.session import Base

class Organization(Base):
    __tablename__ = 'sys_org'

    id = Column(String(20), primary_key=True, index=True)
    tenant_id = Column(String(20), nullable=True)
    parent_id = Column(String(20), nullable=True)
    director_id = Column(String(20), nullable=True)
    name = Column(String(255), nullable=True)
    code = Column(String(255), nullable=True)
    category = Column(String(255), nullable=True)
    sort_code = Column(Integer, nullable=True)
    ext_json = Column(Text, nullable=True)
    delete_flag = Column(String(255), nullable=True)
    create_time = Column(DateTime, nullable=True)
    create_user = Column(String(20), nullable=True)
    update_time = Column(DateTime, nullable=True)
    update_user = Column(String(20), nullable=True)
    ext_attr = Column(Text, nullable=True)