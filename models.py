from pydantic import BaseModel
from typing import List, Optional

class About(BaseModel):
    name: str
    summary: str

class Skill(BaseModel):
    name: str
    level: Optional[str] = None

class SkillsList(BaseModel):
    skills: List[Skill]

class Contact(BaseModel):
    email: str
    telegram_username: Optional[str] = None



























