from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime 
import re

class UserBase(BaseModel):
    email:EmailStr

class UserCreate(UserBase):
    password:str
    @field_validator(password)
    @classmethod
    def password_strength(cls, value:str) -> str:
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase character")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase character")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[^A-Za-z0-9]", value):
            raise ValueError("Password must contain at leasr one special character")

        return value

class UserResponse(UserBase):
    id:int
    is_active:bool
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)

class UserInDB(UserBase):
    id: int
    hashed_password: str
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes= True)
