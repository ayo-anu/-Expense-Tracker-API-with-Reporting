from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, func, Datetime

class TimeStampMixin():
    created_at= Column(Datetime(timezone=true), server_default=func.now())
    updated_at= Column(Datetime(timezone=true), onupdate=func.now())


class Base(DeclarativeBase):
    pass