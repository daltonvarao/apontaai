from ..app.models import BaseModel, db
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(BaseModel):
    __tablename__ = 'usuario'


    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    __password = db.Column("password", db.String(120))
    is_admin = db.Column(db.Boolean, default=False)
    is_authenticated = False
    reclamacoes = db.relationship("Reclamacao", back_populates='usuario')


    @classmethod
    def get_by_email(cls, email):
        return db.session.query(cls).filter_by(email=email).first()

    
    def encrypt_password(self, password):
        self.__password = generate_password_hash(password)


    @property
    def is_anonymous(self):
        return not self.is_authenticated


    @property
    def encrypted_password(self):
        return self.__password


    def authenticate(self, password):
        return check_password_hash(self.__password, password)
