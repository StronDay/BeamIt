from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    
    DEBUG = True

    #############
    # Data-Base #
    #############

    db_name = os.getenv('POSTGRES_DB')
    db_user = os.getenv('POSTGRES_USER')
    db_pass = os.getenv('POSTGRES_PASSWORD')
    db_port = os.getenv('POSTGRES_PORT')
   
    # шаблон переменной: postgresql://<username>:<password>@<host - который в docker>:<port>/<database_name>
    SQLALCHEMY_DATABASE_URI =  f'postgresql://{db_user}:{db_pass}@data_base:{db_port}/{db_name}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

