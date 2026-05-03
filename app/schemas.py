from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None


class ProjectResponse(ProjectCreate):
    id: int

    class Config:
        orm_mode = True