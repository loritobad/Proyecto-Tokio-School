from  flask  import Flask
from .public import public_d
# from .admin import admin
from .clients import clients
from .routes import error404
# from .proveedores import proveedores
#from .clients.models import db




def create_app(entorno ):
    app = Flask(__name__)
    # carga de los parámetros de configuracion
    app.config.from_object(entorno)
    
    #login flask
    #login_manager.init_app(app)

    # inicio base de datos
    #db.init_app(app)
    

    

    # Registro los BluePrints de los módulos
    app.register_blueprint(public_d)
    # app.register_blueprint(admin)
    app.register_blueprint(clients)
    app.register_blueprint(error404)
    # app.register_blueprint(proveedores)
    
    #login_manager.login_view = "clients.login"
    #
    # with app.app_context():
    #     db.create_all()
    
    return app