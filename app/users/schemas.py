from datetime import date
from typing import Annotated, Optional
from fastapi import Query
from pydantic import BaseModel, EmailStr    


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int
    birth_date: date
    
    class Config:
        orm_mode = True

class UserGetSchema(UserBaseSchema):
    id: int

class UserAddSchema(UserBaseSchema):
    pass

class UserUpdateSchema(UserBaseSchema):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None
    birth_date: Optional[date] = None

class UserFilterSchema(BaseModel):
    first_name: Optional[str] = Query(None, description="Фильтр по имени")
    last_name: Optional[str] = Query(None, description="Фильтр по фамилии")
    email: Optional[EmailStr] = Query(None, description="Фильтр по email")
    age: Optional[int] = Query(None, description="Фильтр по возрасту")
    birth_date: Optional[date] = Query(None, description="Фильтр по дате рождения")