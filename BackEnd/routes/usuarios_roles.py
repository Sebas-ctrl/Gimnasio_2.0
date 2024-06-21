from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.usuarios_roles
import crud.usuarios_roles
import crud.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

usuario_rol = APIRouter()

models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario_rol.get("/usuario_rol/", response_model=List[schemas.usuarios_roles.Usuario_Rol], tags=["Usuarios_Roles"])
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.usuarios_roles.get_usuario_roles(db=db, skip=skip, limit=limit)
    return db_users

@usuario_rol.post("/usuario_rol/{id}", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios_Roles"])
def read_usuarios_roles(id: int, db: Session = Depends(get_db)):
    db_user= crud.usuarios_roles.get_usuario_rol(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol not found")
    return db_user

@usuario_rol.post("/usuario_rol/", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios_Roles"])
def create_usuarios_roles(usuarios_roles: schemas.usuarios_roles.Usuario_RolCreate, db: Session = Depends(get_db)):
    db_user = crud.usuarios_roles.get_usuario_rol_by_usuario(db, usuario_rol=usuarios_roles.Usuario_ID)
    if db_user:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return crud.usuarios_roles.create_usuario_rol(db=db, usuario_rol=usuarios_roles)

@usuario_rol.put("/usuario_rol/{id}", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios_Roles"])
def update_usuarios_roles(id: int, roles: schemas.usuarios_roles.Usuario_RolUpdate, db: Session = Depends(get_db)):
    db_user = crud.usuarios_roles.update_usuario_rol(db=db, id=id, rol=roles)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no actualizado")
    return db_user

@usuario_rol.delete("/usuario_rol/{id}", response_model=schemas.usuarios_roles.Usuario_Rol, tags=["Usuarios_Roles"])
def delete_usuarios_roles(id: int, db: Session = Depends(get_db)):
    db_user = crud.usuarios_roles.delete_usuario_rol(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no se pudo eliminar")
    return db_user