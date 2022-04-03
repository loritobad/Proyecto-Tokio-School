from flask import redirect, render_template, request, url_for
from app.clients.forms import LoginClientes
from . import  clients
# vistas de dominio público

@clients.route('/clients',  methods=["GET", "POST"])
def login():
    form = LoginClientes()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("login.html", form=form)

#https://j2logo.com/tutorial-flask-leccion-3-formularios-wtforms/
#https://bootsnipp.com/snippets/z8aQr

