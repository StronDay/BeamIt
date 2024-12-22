from flask import Flask

from .models import data_base
from .routes.users_route import users_route

from .config import Config
from flask_cors import CORS

def create_app():
    
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config())
    data_base.init_app(app)
    app.register_blueprint(users_route)

    with app.app_context():
        # Инициализация базы данных
        data_base.create_all()

    return app