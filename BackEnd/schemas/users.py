from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    id:str
    nombre:str
    primer_apellido: str
    segundo_apellido: str
    direccion: str
    telefono: str
    correo: str
    sangre: str
    fecha_nacimiento: datetime
    created_at:datetime = datetime.now()
    estatus:bool=False

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True