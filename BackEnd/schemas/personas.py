from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class PersonaBase(BaseModel):
    titulo_cortesia: str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    fecha_nacimiento: datetime
    fotografia: str
    genero: str
    tipo_sangre: str
    created_at: datetime
    estatus: bool
    fecha_registro : datetime
    fecha_actualizacion: datetime


class PersonaCreate(PersonaBase):
    pass

class PersonaUpdate(PersonaBase):
    pass

class Persona(PersonaBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


