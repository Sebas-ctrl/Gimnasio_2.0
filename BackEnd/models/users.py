from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__ = "tbb_usuarios"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String(255))
    password = Column(LONGTEXT)
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    Id_persona = Column(Integer)