from .models import data_base
from mongoengine import Document, StringField, UUIDField

import uuid

class TokenModel(data_base.Document):
    meta = {
        'collection': 'tokens'
        # 'id_field': 'user_id'
    }

    # id = None
    user_id = UUIDField(default=uuid.uuid4)
    refresh_token = StringField(required=True)

    def to_dict(self):
        return {
            'user_id': str(self.user_id),
            'refresh_token': self.refresh_token
        }