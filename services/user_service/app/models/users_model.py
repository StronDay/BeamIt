from .models import data_base

import uuid
from sqlalchemy.dialects.postgresql import UUID

class UsersModel(data_base.Model):
    __tablename__ = 'users'
    
    user_id = data_base.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    login = data_base.Column(data_base.String(50), nullable=False)
    passwd = data_base.Column(data_base.String(255), nullable=False)
    email = data_base.Column(data_base.String(50), nullable=False)
    