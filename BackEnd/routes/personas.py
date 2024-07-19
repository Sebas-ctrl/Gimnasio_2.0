from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.personas, config.db, schemas.personas, models.personas
from typing import List

key = Fernet.generate_key()
f = Fernet(key)

persona = APIRouter()
models.personas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para obtener todos los Personas
@persona.get('/personas/', response_model=List[schemas.personas.Persona],tags=['Personas'])
def read_personas(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_personas = crud.personas.get_personas(db=db,skip=skip, limit=limit)
    return db_personas

# Ruta para obtener un Persona por ID
@persona.post("/person/{id}", response_model=schemas.personas.Persona, tags=["Personas"])
def read_person(id: int, db: Session = Depends(get_db)):
    db_person= crud.personas.get_persona(db=db, id=id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

# Ruta para crear un usurio
@persona.post('/personas/', response_model=schemas.personas.Persona,tags=['Personas'])
def create_person(person: schemas.personas.PersonaCreate, db: Session=Depends(get_db)):
    db_personas = crud.personas.get_persona_by_nombre(db,nombre=person.Nombre)
    if db_personas:
        raise HTTPException(status_code=400, detail="Persona existente intenta nuevamente")
    return crud.personas.create_persona(db=db, person=person)

# Ruta para actualizar un Persona
@persona.put('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'])
def update_personas(id:int,person: schemas.personas.PersonaUpdate, db: Session=Depends(get_db)):
    db_personas = crud.personas.update_persona(db=db, id=id, person=person)
    if db_personas is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo actualizar ")
    return db_personas

# Ruta para eliminar un Persona
@persona.delete('/personas/{id}', response_model=schemas.personas.Persona,tags=['Personas'])
def delete_person(id:int, db: Session=Depends(get_db)):
    db_personas = crud.personas.delete_persona(db=db, id=id)
    if db_personas is None:
        raise HTTPException(status_code=404, detail="Persona no existe, no se pudo eliminar ")
    return db_personas