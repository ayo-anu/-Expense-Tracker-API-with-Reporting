from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, func, DateTime

class TimeStampMixin():
    created_at= Column(DateTime(timezone=True), 
    server_default=func.now(),
    nullable=False)

    updated_at= Column(DateTime(timezone=True),
    onupdate=func.now())


class Base(DeclarativeBase):
    pass