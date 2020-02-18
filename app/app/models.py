from datetime import datetime
import importlib
from .db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        db.session.add(self)
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()

    @classmethod
    def get(cls, pk:int):
        return db.session.query(cls).get(pk)

    @classmethod
    def all(cls):
        return db.session.query(cls).all()

    @classmethod
    def last(cls):
        objs = db.session.query(cls).all()
        if objs:
            return objs[-1]
        return None
    
    @classmethod
    def first(cls):
        return db.session.query(cls).first()
