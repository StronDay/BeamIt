# from ..models import UsersModel
# from ..models import data_base
# from ..utils import encrypt_password

# from sqlalchemy.exc import SQLAlchemyError
# from uuid import uuid4

# CIPHER_SERVICE_URL = "http://cipher_service:5002"

# class UserController:
    
#     def create_user(login: str, password: str, email: str):
#         try:
#             encrypted_passwd = encrypt_password(CIPHER_SERVICE_URL, password)
            
#             new_user = UsersModel(
#                 user_id=str(uuid4()),
#                 login=login,
#                 passwd=encrypted_passwd,
#                 email=email
#             )
            
#             data_base.session.add(new_user)
#             data_base.session.commit()
            
#             return new_user
        
#         except SQLAlchemyError as db_err:
#             data_base.session.rollback()
#             return db_err
    
#     def inspect_password():
#         pass
    
#     def get_user():
#         pass
    
#     def get_users():
#         pass