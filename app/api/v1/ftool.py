# -*- coding: utf-8 -*-
"""
@Author: 汪凌峰（Lingfeng Wang）
@Date: 2024/10/13 23:46
定义与工具相关的路由
"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}-/api/v1"}

@router.get("/collector/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}-v1"}