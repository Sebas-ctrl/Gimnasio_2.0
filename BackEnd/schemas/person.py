from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
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

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True