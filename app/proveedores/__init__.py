# creacion e inicilalizacion de blueprint
from flask import Blueprint
#todas las rutas(vistas) del módulo public


proveedores = Blueprint('proveedor', __name__, template_folder='templates/proveedores', static_folder='static')

from . import routes