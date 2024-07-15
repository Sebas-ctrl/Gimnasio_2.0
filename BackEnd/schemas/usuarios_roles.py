from typing import List, Union
from pydantic import BaseModel
from datetime import datetime, date

class Usuario_RolBase(BaseModel):
    Usuario_ID : int
    Rol_ID: int
    #Contrasena: str
    Estatus: bool
    Fecha_Registro : datetime
    Fecha_Actualizacion : datetime
    
class Usuario_RolCreate(Usuario_RolBase):
    pass

class Usuario_RolUpdate(Usuario_RolBase):
    pass

class Usuario_Rol(Usuario_RolBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
