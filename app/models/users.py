from app.db.base import Base
from sqlalchemy.orm import  Mapped, mapped_column, relationship 
from sqlalchemy import String, Text, Integer, Float, Boolean, Date, Enum as SqlEnum 
from datetime import date 
from enum import Enum, IntEnum 
from sqlalchemy.dialects.postgresql import UUID as PG_UUID 
from uuid import uuid4, UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .orders import Order


class Role(str, Enum): 
    admin = 'superuser'
    user = 'user' 
    
class Gender(IntEnum): 
    male = 0 
    female = 1

class User(Base):

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4, index=True) 
    role: Mapped[Role] = mapped_column(SqlEnum(Role, name='role_enum'), nullable=False) 
    gender: Mapped[Gender] = mapped_column(SqlEnum(Gender, name='gender_enum'), nullable=False) 
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(20), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False) 
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False) 
    address: Mapped[str | None] = mapped_column(String(200)) 
    introduction: Mapped[str | None] = mapped_column(Text) 
    height: Mapped[float | None] = mapped_column(Float) 
    weight: Mapped[float | None] = mapped_column(Float) 
    birthday: Mapped[date | None] = mapped_column(Date) 

    orders_rel: Mapped[list["Order"]] = relationship(back_populates="user_rel", cascade="all, delete-orphan", passive_deletes=True)




