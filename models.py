from app import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Messages(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str]
  email: Mapped[str]
  message: Mapped[str]

class Projects(db.Model):
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str]
  description: Mapped[str]
  icon: Mapped[str]
  link: Mapped[str]
