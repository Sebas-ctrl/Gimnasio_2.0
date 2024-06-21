import models.roles
import schemas.roles
from sqlalchemy.orm import Session
import models, schemas

def get_rol(db: Session, id: int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()

def get_rol_by_usuario(db: Session, nombre: str):
    return db.query(models.roles.Rol).filter(models.roles.Rol.Nombre == nombre).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: schemas.roles.RolCreate):
    db_user = models.roles.Rol(
                                Nombre = rol.Nombre,
                                Descripcion=rol.Descripcion, 
                                #Contrasena=rol.Contrasena, 
                                Estatus=rol.Estatus, 
                                Fecha_Registro=rol.Fecha_Registro,
                                Fecha_Actualizacion=rol.Fecha_Actualizacion
                                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_rol(db: Session, id: int, rol: schemas.roles.RolUpdate):
    db_user = db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()
    if db_user:
        for var, value in vars(rol).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_rol(db: Session, id: int):
    db_user = db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user