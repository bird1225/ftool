# -*- coding: utf-8 -*-
# @Author  : 汪凌峰(Lingfeng Wang)
# @Date    : 2024/11/8 17:13
# app/services/organization_service.py
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.org import Organization  # 确保导入你的模型
from datetime import datetime
import uuid

class OrganizationService:
    def __init__(self, db: Session):
        self.db = db

    def get_organization_by_id(self, org_id: str):
        return self.db.query(Organization).filter(Organization.id == org_id).first()

    def get_all_organizations(self):
        return self.db.query(Organization).all()

    def create_organization(self, tenant_id: str, parent_id: str, director_id: str, name: str, code: str,
                            category: str, sort_code: int, ext_json: str, create_user: str):
        new_org = Organization(
            id=str(uuid.uuid4()),  # 生成唯一ID
            tenant_id=tenant_id,
            parent_id=parent_id,
            director_id=director_id,
            name=name,
            code=code,
            category=category,
            sort_code=sort_code,
            ext_json=ext_json,
            delete_flag='0',  # 默认未删除
            create_time=datetime.now(),
            create_user=create_user
        )
        self.db.add(new_org)
        self.db.commit()
        self.db.refresh(new_org)
        return new_org

    def update_organization(self, org_id: str, name: str, code: str, category: str, sort_code: int,
                            update_user: str):
        org = self.get_organization_by_id(org_id)
        if org:
            org.name = name
            org.code = code
            org.category = category
            org.sort_code = sort_code
            org.update_time = datetime.now()
            org.update_user = update_user
            self.db.commit()
            self.db.refresh(org)
            return org
        return None

    def delete_organization(self, org_id: str):
        org = self.get_organization_by_id(org_id)
        if org:
            org.delete_flag = '1'  # 逻辑删除