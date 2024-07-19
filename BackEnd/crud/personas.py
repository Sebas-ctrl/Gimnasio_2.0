import models.personas
import schemas.personas
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_persona(db:Session, id: int):
    return db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()

# Busqueda por Nombre
def get_persona_by_nombre(db:Session, nombre: str):
    return db.query(models.personas.Persona).filter(models.personas.Persona.Nombre == nombre).first()

# Buscar todos las personas
def get_personas(db:Session, skip: int=0, limit:int=10):
    return db.query(models.personas.Persona).offset(skip).limit(limit).all()

# Crear una nueva personas
def create_persona(db:Session, person: schemas.personas.PersonaCreate):
    db_person = models.personas.Persona(Titulo_Cortesia=person.Titulo_Cortesia,
                                      Nombre=person.Nombre, 
                                      Primer_Apellido=person.Primer_Apellido, 
                                      Segundo_Apellido=person.Segundo_Apellido, 
                                      Fecha_Nacimiento=person.Fecha_Nacimiento, 
                                      Fotografia=person.Fotografia, 
                                      Genero=person.Genero,
                                      Tipo_Sangre=person.Tipo_Sangre, 
                                      Estatus=person.Estatus,
                                      Fecha_Registro=person.Fecha_Registro,
                                      Fecha_Actualizacion=person.Fecha_Actualizacion)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# Actualizar una personas por id
def update_persona(db:Session, id:int, person:schemas.personas.PersonaUpdate):
    db_person = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

# Eliminar una personas por id
def delete_persona(db:Session, id:int):
    db_person = db.query(models.personas.Persona).filter(models.personas.Persona.ID == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person