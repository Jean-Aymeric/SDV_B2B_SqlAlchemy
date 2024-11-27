from tkinter.tix import INTEGER
from winreg import EnumKey

from sqlalchemy import ForeignKey, Date, String, Enum
from sqlalchemy.orm import Session, Mapped, mapped_column

from database import Engine
from database.model.AbstractEntity import AbstractEntity


class Employee(AbstractEntity):
    __tablename__ = 'pata_employees'
    emp_no: Mapped[str] = mapped_column(primary_key=True)
    birth_date: Mapped[str] = mapped_column(Date)
    first_name: Mapped[str] = mapped_column(String(14))
    last_name: Mapped[str] = mapped_column(String(16))
    gender: Mapped[str] = mapped_column(Enum('M', 'F'))
    hire_date: Mapped[str] = mapped_column(Date)
    salary: Mapped[int] = mapped_column(INTEGER)
    title: Mapped[str] = mapped_column(String(50))
    dept_no: Mapped[str] = mapped_column(ForeignKey('pata_departments.dept_no'))

    @property
    def Emp_no(self) -> str:
        return self.emp_no

    @property
    def Birth_date(self) -> str:
        return self.birth_date

    @property
    def First_name(self) -> str:
        return self.first_name

    @property
    def Last_name(self) -> str:
        return self.last_name

    @property
    def Gender(self) -> str:
        return self.gender

    @property
    def Hire_date(self) -> str:
        return self.hire_date

    @property
    def Salary(self) -> int:
        return self.salary

    @property
    def Title(self) -> str:
        return self.title

    @property
    def Dept_no(self) -> str:
        return self.dept_no

    @classmethod
    def getAll(cls):
        with Session(Engine.getEngine()) as session:
            return session.query(cls).all()

    def __repr__(self):
        return (f"Employee(emp_no={self.emp_no}, "
                f"birth_date={self.birth_date}, "
                f"first_name={self.first_name}, "
                f"last_name={self.last_name}, "

    def toDict(self):
        return {
            "emp_no": self.emp_no,
            "birth_date": self.birth_date,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender": self.gender,
            "hire_date": self.hire_date,
            "salary": self.salary,
            "title": self.title,
            "dept_no": self.dept_no
        }