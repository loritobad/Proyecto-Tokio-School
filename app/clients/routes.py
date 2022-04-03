from flask import render_template
from . import  clients
from forms import LoginClientes
# vistas de dominio público

@clients.route('/clients')
def index():
    return render_template('login.html')


