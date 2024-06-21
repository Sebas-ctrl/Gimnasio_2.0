import models.roles
import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session
import models, schemas

def get_usuario_rol(db: Session, id: int):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.ID == id).first()

def get_usuario_rol_by_usuario(db: Session, usuario_rol: str):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.Usuario_ID == usuario_rol).first()

def get_usuario_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.usuarios_roles.Usuario_Rol).offset(skip).limit(limit).all()

def create_usuario_rol(db: Session, usuario_rol: schemas.usuarios_roles.Usuario_RolCreate):
    db_user = models.usuarios_roles.Usuario_Rol(
                                Usuario_ID = usuario_rol.Usuario_ID,
                                Rol_ID = usuario_rol.Rol_ID,
                                Estatus=usuario_rol.Estatus, 
                                Fecha_Registro=usuario_rol.Fecha_Registro,
                                Fecha_Actualizacion=usuario_rol.Fecha_Actualizacion
                                )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_usuario_rol(db: Session, id: int, rol: schemas.usuarios_roles.Usuario_RolUpdate):
    db_user = db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.ID == id).first()
    if db_user:
        for var, value in vars(rol).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_usuario_rol(db: Session, id: int):
    db_user = db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user