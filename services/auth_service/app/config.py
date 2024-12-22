from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    
    DEBUG = True
    
    MONGODB_SETTINGS = {
        'db': os.getenv('MONGO_DB'),
        'host': 'mongo_db',
        'port': int(os.getenv('MONGO_PORT'))
    }

    algorithm = os.getenv('JWT_ALGORITHM')
    access_key = os.getenv('JWT_ACCESS_KEY')
    refresh_key = os.getenv('JWT_REFRESH_KEY')