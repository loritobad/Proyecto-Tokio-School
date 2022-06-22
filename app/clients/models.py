from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# objeto de base de datos
#db = SQLAlchemy()

#relaciones entre tablas

# Modelos para el paquete clientes
# class Cliente(db.Model, UserMixin):
#     __tablename__ = 'clientes'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(256), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)
#     is_admin = db.Column(db.Boolean, default=False)

