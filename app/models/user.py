from sqlmodel import Field, Relationship
from typing import Optional, List

class User(table=True):
    id: int = Field(default=None, primary_key=True)
    role_id: int = Field(foreign_key="role.id")
    user: Optional["User"] = Relationship(back_populates="role")