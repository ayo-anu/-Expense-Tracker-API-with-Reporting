from pydantic import BaseModel, field_validator
from datetime import datetime
from decimal import Decimal

from app.model.expense import ExpenseCategory

class ExpenseBase(BaseModel):
    amount:Decimal
    category:ExpenseCategory
    description:str|None = None
    expense_date:datetime

    @field_validator("amount")
    @classmethod
    def amount_must_be_positive(cls, value:Decimal) -> Decimal:
        if value <= 0:
            raise ValueError("Amount must be greater than zero")
        if value > Decimal("999999.99"):
            raise ValueError("Amount exceeds maximum allowed value")
        return round(value, 2)

class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(BaseModel):
    amount:Decimal | None = None
    category:ExpenseCategory | None = None
    decription:str | None = None
    expense_date:datetime | None = None

    @field_validator("amount")
    @classmethod
    def amount_must_not_be_zero(cls, value:Decimal|None) -> Decimal | None:
        if value is None:
            return None
        if value <= 0:
            raise ValueError("Amount must be greater than 0 or None")
        return round(value, 2)

class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


