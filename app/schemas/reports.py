from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class CategorySummary(BaseModel):
    category:str
    total_amount:Decimal
    transaction_count:int
    percentage_of_total:Decimal

    model_config = configDict(from_attributes=True)

class MonthlySummary(BaseModel):
    year: int
    month: int
    total_amount: Decimal
    transaction_count: int

    model_config = configDict(from_attributes=True)

class SpendingTrend(BaseModel):
    period: str
    total_amount: Decimal
    transaction_count: int

    model_config = configDict(from_attributes=True)

class ReportResponse(BaseModel):
    user_id:int
    generated_at:datetime
    category_breakdown:list[CategorySummary]
    monthly_summary: list[MonthlySummary]

    model_config = configDict(from_attributes=True)



    