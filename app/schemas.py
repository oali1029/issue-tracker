from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True


class IssueCreate(BaseModel):
    title: str
    description: str
    priority: str
    owner_id: int

class IssueResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    status: str
    created_at: datetime
    closed_at: Optional[datetime]

    class Config:
        from_attributes = True
