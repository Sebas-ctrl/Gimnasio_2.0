import models.personas
import schemas.personas
from sqlalchemy.orm import Session
import models, schemas

def get_persona(db: Session, id: int):
    return db.query(models.personas.Persona).filter(models.personas.Persona.id == id).first()

def get_persona_by_id(db: Session, nombre: str):
    return db.query(models.personas.Persona).filter(models.personas.Persona.nombre == nombre).first()

def get_personas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.personas.Persona).offset(skip).limit(limit).all()

def create_personas(db: Session, nom: schemas.personas.PersonaCreate):
    db_user = models.personas.Persona(titulo_cortesia=nom.titulo_cortesia, nombre=nom.nombre,primer_apellido=nom.primer_apellido, segundo_apellido=nom.segundo_apellido,fecha_nacimiento=nom.fecha_nacimiento,  fotografia=nom.fotografia,  genero=nom.genero,  tipo_sangre=nom.tipo_sangre, created_at=nom.created_at, estatus=nom.estatus, fecha_registro=nom.fecha_registro, fecha_actualizacion=nom.fecha_actualizacion )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_personas(db: Session, id: int, person: schemas.personas.PersonaUpdate):
    db_user = db.query(models.personas.Persona).filter(models.personas.Persona.id == id).first()
    if db_user:
        for var, value in vars(person).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_personas(db: Session, id: int):
    db_user = db.query(models.personas.Persona).filter(models.personas.Persona.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user