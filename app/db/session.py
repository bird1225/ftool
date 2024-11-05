# -*- coding: utf-8 -*-
"""
@Author: 汪凌峰（Lingfeng Wang）
@Date: 2024/10/13 23:50
数据库会话和初始化，临时使用MySQL，后续可能会考虑更换为pg
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.config import config

# 创建数据库引擎
engine = create_engine(
    config.DATABASE_URL,
    pool_size=10,            # 设置连接池大小
    max_overflow=20,         # 允许的最大连接数
    pool_timeout=30,         # 连接超时时间
    pool_recycle=1800,       # 回收时间，避免连接断开
    pool_pre_ping=True       # 自动检查连接有效性
)


# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建Base类,用于声明模型
Base = declarative_base()

# 获取数据库会话的函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == '__main__':
    print(config.DB_HOST)
    print(config.DATABASE_URL)
    # db = next(get_db())
    # print("Database connection successful:", db)