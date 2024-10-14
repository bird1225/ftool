# -*- coding: utf-8 -*-
"""
@Author: 汪凌峰（Lingfeng Wang）
@Date: 2024/10/13 23:46
配置文件（例如数据库、环境变量）
"""

from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

settings = Settings()