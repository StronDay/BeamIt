from flask import Flask

from app.routes import token_route
from app.routes import auth_route
from app.models.models import data_base

from .config import Config

def create_app():
   
   app = Flask(__name__)
   
   app.config.from_object(Config())
   
   app.register_blueprint(token_route)
   app.register_blueprint(auth_route)
   
   data_base.init_app(app)
   # with app.app_context():
   #    data_base.create_all()
    
   return app