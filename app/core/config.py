# -*- coding: utf-8 -*-
"""
@Author: 汪凌峰（Lingfeng Wang）
@Date: 2024/10/13 23:46
配置文件（例如数据库、环境变量）
"""
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


# 手动加载 .env 文件
load_dotenv(".env")

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

# 实例化配置
config = Settings()
