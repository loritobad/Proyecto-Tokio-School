import os


class BaseConfig(object):
    USER_APP_NAME = 'FlaskMalcen'
    USER_ENABLE_EMAIL = True
    'Base configuracion'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI= "sqlite:///"+os.path.join(BASE_DIR + '\\app\\db\\',  "gestor.sqlite")
   
    #WTF_CSRF_TIME_LIMIT = 10
class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = False
    TESTING = True
    SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False