from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.roles
import crud.roles, config.db, schemas.roles, models.roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

rol = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol.get("/rol/", response_model=List[schemas.roles.Rol], tags=["Roles"])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_users

@rol.post("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def read_roles(id: int, db: Session = Depends(get_db)):
    db_user= crud.roles.get_rol(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol not found")
    return db_user

@rol.post("/rol/", response_model=schemas.roles.Rol, tags=["Roles"])
def create_roles(roles: schemas.roles.RolCreate, db: Session = Depends(get_db)):
    db_user = crud.roles.get_rol_by_usuario(db, nombre=roles.Nombre)
    if db_user:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return crud.roles.create_rol(db=db, rol=roles)

@rol.put("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def update_roles(id: int, roles: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_user = crud.roles.update_rol(db=db, id=id, rol=roles)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no actualizado")
    return db_user

@rol.delete("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def delete_roles(id: int, db: Session = Depends(get_db)):
    db_user = crud.roles.delete_rol(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no se pudo eliminar")
    return db_user