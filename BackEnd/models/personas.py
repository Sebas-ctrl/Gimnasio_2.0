from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    titulo_cortesia = Column(String(255))
    nombre = Column(String(255))
    primer_apellido = Column(String(255))
    segundo_apellido = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    fotografia = Column(String(255))
    genero = Column(String(255))
    tipo_sangre = Column(String(255))
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea


