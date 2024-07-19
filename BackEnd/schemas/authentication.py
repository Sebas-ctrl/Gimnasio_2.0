from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class AuthBase(BaseModel):
    correo: str
    contrasena: str

class AuthCreate(AuthBase):
    pass

class AuthUpdate(AuthBase):
    pass

class User(AuthBase):
    id: int

    class Config:
        orm_mode = True