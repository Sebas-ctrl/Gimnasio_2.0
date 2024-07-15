from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.personas
import crud.personas, config.db, schemas.personas, models.personas
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

persona = APIRouter()

models.personas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@persona.get("/personas/", response_model=List[schemas.personas.Persona], tags=["Personas"])
def read_persnas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= crud.personas.get_personas(db=db, skip=skip, limit=limit)
    return db_users

@persona.post("/persona/{id}", response_model=schemas.personas.Persona, tags=["Personas"])
def read_persona(id: int, db: Session = Depends(get_db)):
    db_user= crud.personas.get_personas(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_user

@persona.post("/persona/", response_model=schemas.personas.Persona, tags=["Personas"])
def create_persona(persona: schemas.personas.PersonaCreate, db: Session = Depends(get_db)):
    db_user = crud.personas.get_persona_by_id(db, nombre=persona.nombre)
    if db_user:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.personas.create_personas(db=db, nom=persona)

@persona.put("/persona/{id}", response_model=schemas.personas.Persona, tags=["Personas"])
def update_persona(id: int, persona: schemas.personas.PersonaUpdate, db: Session = Depends(get_db)):
    db_user = crud.personas.update_personas(db=db, id=id, person=persona)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no actualizado")
    return db_user

@persona.delete("/persona/{id}", response_model=schemas.personas.Persona, tags=["Personas"])
def delete_persona(id: int, db: Session = Depends(get_db)):
    db_user = crud.personas.delete_personas(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar")
    return db_user