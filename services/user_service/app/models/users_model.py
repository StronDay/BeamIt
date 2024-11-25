from .models import data_base

class UsersModel(data_base.Model):
    __tablename__ = 'users'
    
    user_id = data_base.Column(data_base.String(1000), primary_key=True)
    login = data_base.Column(data_base.String(50))
    passwd = data_base.Column(data_base.String(50))
    email = data_base.Column(data_base.String(50))
    