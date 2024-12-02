from ..models.users_model import UsersModel
from sqlalchemy.exc import SQLAlchemyError
from uuid import uuid4
from flask import jsonify

def is_user_existing(login, email):
    """Проверяет существование пользователя с данным логином или email."""
    return UsersModel.query.filter(
        (UsersModel.login == login) | (UsersModel.email == email)
    ).first()

def create_new_user(data_base, login, encrypted_passwd, email):
    """Создаёт и сохраняет нового пользователя в БД."""
    try:
        new_user = UsersModel(
            user_id=str(uuid4()),
            login=login,
            passwd=encrypted_passwd,
            email=email
        )
        data_base.session.add(new_user)
        data_base.session.commit()
        return new_user
    except SQLAlchemyError as db_err:
        data_base.session.rollback()
        raise db_err
    
def get_user_password(login):
    user = UsersModel.query.filter(
        (UsersModel.login == login) | (UsersModel.email == login)
    ).first()
    
    if user:
        return user.passwd
    else:
        return None