from sqlalchemy import String, text
from sqlalchemy.orm import Mapped, Session
from sqlalchemy.testing.schema import mapped_column

from database import Engine
from database.model.AbstractEntity import AbstractEntity


class Bidule(AbstractEntity):
    __tablename__ = "bidule"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    @property
    def Id(self) -> int:
        return self.id

    @property
    def Name(self) -> str:
        return self.name

    def __repr__(self):
        return f"Bidule(id={self.id}, name={self.name})"

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def insert(self):
        with Session(Engine.getEngine()) as session:
            result = session.execute(text('CALL addBidule(:name)'), {'name': self.Name})
            results = result.fetchall()
            session.commit()
            self.id = results[0][0]
            return self
