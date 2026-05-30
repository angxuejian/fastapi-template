from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .users import User
    from .permissions import Permission


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    users_rel: Mapped[list["User"]] = relationship(secondary="user_roles", back_populates="roles_rel")
    permissions_rel: Mapped[list["Permission"]] = relationship(secondary="role_permissions", back_populates="roles_rel")
    