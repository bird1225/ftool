# -*- coding: utf-8 -*-
"""
@Author: 汪凌峰（Lingfeng Wang）
@Date: 2024/10/13 23:48
工具相关的数据模型
"""
from sqlalchemy import Column, Integer, String
from app.db.base_class import Base

class Tool(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)