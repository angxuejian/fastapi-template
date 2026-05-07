from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import TIMESTAMP, func, DateTime

from datetime import datetime


class Base(DeclarativeBase): 
    __abstract__ = True 

    # TIMESTAMP(timezone=True): sql层 
    created_time: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False, index=True) 

    # DateTime(timezone=True): orm层 
    updated_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False, index=True)