from flask import render_template
from . import public_d


# vistas de dominio público

# componente que gestiona los login


@public_d.route('/')
def index():
    return render_template('index.html')