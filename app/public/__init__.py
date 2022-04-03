# creacion e inicilalizacion de blueprint
from flask import Blueprint
#todas las rutas(vistas) del módulo public


public_d = Blueprint('public_d', __name__, template_folder='templates/public', static_folder='static')

from . import routes
