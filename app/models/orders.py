from app.db.base import Base;
from sqlalchemy.orm import Mapped, mapped_column, relationship 
from sqlalchemy import ForeignKey
from uuid import  UUID
from .users import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User

class Order(Base):

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True) 
    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id', ondelete="CASCADE")) 
    user_rel: Mapped["User"] = relationship(back_populates="orders_rel")