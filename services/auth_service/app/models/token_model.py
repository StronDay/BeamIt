from .models import data_base

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

class TokenModel(data_base.Model):
    __tablename__ = 'tokens'

    user_id = data_base.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    refresh_token = data_base.Column(data_base.Text, nullable=False)
    
    def to_dict(self):
        return {
            'user_id': self.user_id,
            'refresh_token': self.refresh_token
        }