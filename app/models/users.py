from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import BaseModel
from sqlalchemy import String, Integer


class Users(BaseModel):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    age: Mapped[int] = mapped_column(Integer)




