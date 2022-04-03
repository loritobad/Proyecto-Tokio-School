from flask import render_template
from . import  admin

# vistas de dominio público

@admin.route('/admin')
def index():
    return "<p>ona admin - logueo ee ide3ntificacion </p>"