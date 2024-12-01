from sqlalchemy.exc import IntegrityError
from datetime import timedelta, datetime, timezone

from app.models.token_model import TokenModel
from app.models.models import data_base

from flask import current_app
import jwt
import time

from dotenv import load_dotenv
import os

class Token():
    
    def __init__(self):
        
        # algorithm = os.getenv('JWT_ALGORITHM')
        # access_key = os.getenv('JWT_ACCESS_KEY')
        # refresh_key = os.getenv('JWT_REFRESH_KEY')
        
        self._algorithm = os.getenv('JWT_ALGORITHM')
        self._access_key = os.getenv('JWT_ACCESS_KEY')
        self._refresh_key = os.getenv('JWT_REFRESH_KEY')
    
    def generateAccess(self, payload: dict):
        
        payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=5)
        
        token = jwt.encode(payload, self._access_key, self._algorithm)
        return token
    
    def generateRefresh(self, payload: dict):
        
        payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=2)
        
        token = jwt.encode(payload, self._refresh_key, self._algorithm)
        return token
    

    def saveToken(self, user_id, refresh_token):
        try:
            token_record = TokenModel.query.filter_by(user_id=user_id).first()

            if token_record:
                token_record.refresh_token = refresh_token
            else:
                token_record = TokenModel(user_id=user_id, refresh_token=refresh_token)
                data_base.session.add(token_record)

            data_base.session.commit()
            
            return True

        except IntegrityError as e:
            data_base.session.rollback()
            return {"error": "User not found, invalid user_id"}, 400
        except Exception as e:
            data_base.session.rollback()
            return {"error": str(e)}, 500
            
        