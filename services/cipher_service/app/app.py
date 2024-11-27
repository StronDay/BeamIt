from flask import Flask

from .routes.cipher_route import cipher_route

from .config import Config
from flask_cors import CORS

def create_app():
   
   app = Flask(__name__)
   CORS(app)
   
   app.config.from_object(Config())
   app.register_blueprint(cipher_route)
    
   return app