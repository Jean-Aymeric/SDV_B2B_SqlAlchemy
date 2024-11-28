from sqlalchemy.orm import DeclarativeBase, Session

from database import Engine


class AbstractEntity(DeclarativeBase):
    @classmethod
    def getAll(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    @classmethod
    def getById(cls, id):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).get(id)