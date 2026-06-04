from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship

from app.db.base import TimeStampMixin, Base

import enum

class ExpenseCategory(str, enum.Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    HOUSING = "housing"
    HEALTHCARE = "healthcare"
    ENTERTAINMENT = "entertainment"
    UTILITIES = "utilities"
    EDUCATION = "education"
    OTHER = "other"

class Expense(TimeStampMixin, Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    amount = Column(Numeric(precision=10, scale=2), nullable=False)
    category = Column(SQLEnum(ExpenseCategory), nullable=False)
    description = Column(String(500), nullable=True)
    expense_date = Column(DateTime(timezone=True), nullable=False)

    owner = relationship("User", back_populates="expenses")

    def __repr__(self):
        return f"<Expense id={self.id} amount={self.amount} category={self.category}>"