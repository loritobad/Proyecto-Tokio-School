from flask import render_template, Blueprint


error404 = Blueprint('error404', __name__)

#errores NO ENCONTRADO
@error404.app_errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('pag404.html'), 404