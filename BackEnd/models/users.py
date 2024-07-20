from sqlalchemy import Column, Integer, String,  DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import enum



class MyEstatus(str, enum.Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"



class User(Base):
    __tablename__ = "tbb_usuarios"

    ID = Column(Integer, primary_key=True, index=True)
    Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Nombre_Usuario = Column(String(255))
    Correo_Electronico = Column(String(100))
    Contrasena = Column(String(40))
    Numero_Telefonico_Movil = Column(String(20))
    Estatus = Column( Enum(MyEstatus))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    
    #items = relationship("Item", back_populates="owner") Clave Foranea




