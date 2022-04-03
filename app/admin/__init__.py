# creacion e inicilalizacion de blueprint
from flask import Blueprint

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

#todas las rutas(vistas) del paquete public
from . import routes