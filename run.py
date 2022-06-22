
from config import DevelopmentConfig

from .app import create_app




# punto de entrada a la APP
app = create_app(entorno=DevelopmentConfig)