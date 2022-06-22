from urllib.parse import urlparse
from flask import redirect, render_template, request, url_for
import flask
from app.clients.forms import LoginClientes
from app.clients.models import Cliente
from . import  clients
from flask_login import LoginManager, logout_user, login_user, login_required


# componente que gestiona los login
#login_manager = LoginManager()

@clients.route('/clients',  methods=["GET", "POST"])
def login():
    form = LoginClientes()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        
        #login_user(Cliente)
        print('LOGUEADOOOOOOOOOOOOOOOOOOOOOOO')
        
        
        next_page = request.args.get('next', None)
        if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('login_client.client')
                return redirect(next_page)
    return render_template("login.html", form=form)

# @clients.route("/settings")
# @login_required
# def settings():
#     pass

