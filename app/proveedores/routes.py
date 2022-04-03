from flask import render_template
from . import proveedores

# vistas de proveedores

@proveedores.route('/proveedores')
def index():
    return "<p>zona provedor</p>"