from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.person, config.db, schemas.person, models.person
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

person = APIRouter()
models.person.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@person.get("/persons/", response_model=List[schemas.users.User], tags=["Personas"])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_persons = crud.person.get_persons(db=db, skip=skip, limit=limit)
    return db_persons

@user.post("/person/{id}", response_model=schemas.users.User, tags=["Personas"])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.person.get_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@user.post("/persons/", response_model=schemas.person.Person, tags=["Personas"])
def create_person(person: schemas.person.PersonCreate, db: Session = Depends(get_db)):
    db_person = crud.person.get_person_by_nombre(db, nombre=person.nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.person.create_person(db=db, person=person)

@user.put("/person/{id}", response_model=schemas.person.Person, tags=["Personas"])
def update_user(id: int, user: schemas.person.PersonUpdate, db: Session = Depends(get_db)):
    db_person = crud.person.update_person(db=db, id=id, user=user)
    if db_person:
        raise HTTPException(status_code=400, detail="Persona no existe, no se pudo actualizar")
    return db_person

@user.delete("/person/{id}", response_model=schemas.person.Person, tags=["Personas"])
def delete_person(id: int, db: Session = Depends(get_db)):
    db_person = crud.person.delete_person(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail = "Usuario no existe, no se pudo eliminar")
    return db_person