from flask import Flask
from .public import public_d
from .admin import admin
from .clients import clients
from .routes import error404
from .proveedores import proveedores




# creo la APP

def create_app():
    app = Flask(__name__)

    # configuracion flask-wtk
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    
    # Registro los BluePrints de los módulos
    app.register_blueprint(public_d)
    app.register_blueprint(admin)
    app.register_blueprint(clients)
    app.register_blueprint(error404)
    app.register_blueprint(proveedores)
    
    app.run(debug=True)
    
    return app