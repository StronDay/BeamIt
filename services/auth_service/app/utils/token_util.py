# from sqlalchemy.exc import IntegrityError
from datetime import timedelta, datetime, timezone

from app.models.token_model import TokenModel
from app.models.models import data_base

from flask import current_app
import jwt
import time

from mongoengine import DoesNotExist

from dotenv import load_dotenv
import os

class TokenUtil():
    
    def __init__(self):
        
        self._algorithm = os.getenv('JWT_ALGORITHM')
        self._access_key = os.getenv('JWT_ACCESS_KEY')
        self._refresh_key = os.getenv('JWT_REFRESH_KEY')
    
    def generateAccess(self, payload: dict):
        
        payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=1)
        
        token = jwt.encode(payload, self._access_key, self._algorithm)
        return token
    
    def generateRefresh(self, payload: dict):
        
        payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=2)
        
        token = jwt.encode(payload, self._refresh_key, self._algorithm)
        return token
    
    def inspectRefresh(self, refresh_token):
        try:
            return jwt.decode(refresh_token, self._refresh_key, self._algorithm)
        except Exception as e:
            return None

    def inspectAccess(self, access_token):
        try:
            return jwt.decode(access_token, self._access_key, self._algorithm)
        except Exception as e:
            return None
        
    # def find_token(self, refresh_token):
    #     token = TokenModel.query.filter_by(refresh_token=refresh_token).first()
    #     if not token:
    #         return None
        
    #     token_data = token.to_dict()
    #     return self.inspectRefresh(token_data["refresh_token"])
    
    # def delete_token(self, refresh_token):
    #     try:
    #         # Находим запись по значению токена
    #         token_record = TokenModel.query.filter_by(refresh_token=refresh_token).first()
            
    #         if token_record:
    #             data_base.session.delete(token_record)  # Удаляем запись
    #             data_base.session.commit()  # Сохраняем изменения
    #             return {"message": refresh_token}, 200
    #         else:
    #             return {"error": "Token not found"}, 404

    #     except Exception as e:
    #         data_base.session.rollback()  # Откатываем сессию в случае ошибки
    #         return {"error": str(e)}, 500

    # def saveToken(self, user_id, refresh_token):
    #     try:
    #         token_record = TokenModel.query.filter_by(user_id=user_id).first()

    #         if token_record:
    #             token_record.refresh_token = refresh_token
    #         else:
    #             token_record = TokenModel(user_id=user_id, refresh_token=refresh_token)
    #             data_base.session.add(token_record)

    #         data_base.session.commit()
            
    #         return True
        
    #     except Exception as e:
    #         data_base.session.rollback()
    #         return {"error": str(e)}, 500
            
    def find_token(self, refresh_token):
        try:
            # Находим токен по значению refresh_token
            token = TokenModel.objects.get(refresh_token=refresh_token)
            token_data = token.to_dict()
            return self.inspectRefresh(token_data["refresh_token"])
        except DoesNotExist:
            return None

    def delete_token(self, refresh_token):
        try:
            # Находим запись по значению токена
            token_record = TokenModel.objects.get(refresh_token=refresh_token)
            token_record.delete()  # Удаляем запись
            return {"message": refresh_token}, 200
        except DoesNotExist:
            return {"error": "Token not found"}, 404
        except Exception as e:
            return {"error": str(e)}, 500

    def saveToken(self, user_id, refresh_token):
        try:
            # Находим запись по user_id
            token_record = TokenModel.objects(user_id=user_id).first()

            if token_record:
                token_record.refresh_token = refresh_token
                token_record.save()  # Сохраняем изменения
            else:
                token_record = TokenModel(user_id=user_id, refresh_token=refresh_token)
                token_record.save()  # Сохраняем новый токен

            return True
        except Exception as e:
            return {"error": str(e)}, 500
        