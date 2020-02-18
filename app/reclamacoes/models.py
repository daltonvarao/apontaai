from ..app.db import db
from ..app.models import BaseModel


class Reclamacao(BaseModel):
    __tablename__ = 'reclamacao'

    def __init__(titulo=None, descricao=None, local=None, usuario=None):
        pass

    titulo = db.Column(db.String)
    descricao = db.Column(db.String)
    local = db.Column(db.String)
    fechada = db.Column(db.Boolean, default=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', back_populates="reclamacoes")
