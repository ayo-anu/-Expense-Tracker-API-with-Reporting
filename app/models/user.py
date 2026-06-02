from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base import TimeStampMixin, Base

class User(TimeStampMixin, Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    expenses = relationship("Expense", back_populates="owner", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User id={self.id}  email={self.email}"