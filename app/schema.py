from pydantic import BaseModel, Field
from typing import List, Optional
from enums import PhoneType, ContactCategory


class PhoneCreate(BaseModel):
    number: str
    type: PhoneType


class PhoneRead(PhoneCreate):
    id: int

    class Config:
        orm_mode = True


class ContactCreate(BaseModel):
    name: str
    category: ContactCategory
    phones: List[PhoneCreate] = Field(default_factory=list)


class ContactRead(BaseModel):
    id: int
    name: str
    category: ContactCategory
    phones: List[PhoneRead]

    class Config:
        orm_mode = True
