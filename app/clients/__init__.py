# creacion e inicilalizacion de blueprint
from flask import Blueprint


clients = Blueprint('client', __name__, template_folder='templates/clients', static_folder='static')

#todas las rutas(vistas) del paquete public
from . import routes