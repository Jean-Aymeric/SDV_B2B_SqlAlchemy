from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Session, Mapped, mapped_column

from database import Engine
from database.model.AbstractEntity import AbstractEntity


class Department(AbstractEntity):
    __tablename__ = 'pata_departments'
    dept_no: Mapped[str] = mapped_column(primary_key=True)
    dept_name: Mapped[str] = mapped_column(String(40))
    emp_no: Mapped[int] = mapped_column(ForeignKey('pata_employees.emp_no'))

    @property
    def Dept_no(self) -> str:
        return self.dept_no

    @property
    def Dept_name(self) -> str:
        return self.dept_name

    @property
    def Emp_no(self) -> int:
        return self.emp_no

    @classmethod
    def getAll(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return f"Department(dept_no={self.dept_no}, dept_name={self.dept_name}, emp_no={self.emp_no})"

    def toDict(self):
        return {
            "dept_no": self.dept_no,
            "dept_name": self.dept_name,
            "emp_no": self.emp_no
        }