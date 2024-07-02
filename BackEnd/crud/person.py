import models.person
import schemas.person
from sqlalchemy.orm import Session
import models, schemas

def get_person(db: Session, id: int):
    return db.query(models.person.Person).filter(models.person.Person.id == id).first()

def get_person_by_nombre(db: Session, nombre: str):
    return db.query(models.person.Person).filter(models.person.Person.nombre == nombre).first()

def get_persons(db: Session, skip: int = 0, limit: int = 0):
    return db.query(models.person.Person).offset(skip).limit(limit).all()

def create_person(db: Session, person: schemas.person.PersonUpdate):
    db_person = models.person.Person(nombre=person.nombre, primer_apellido=person.primer_apellido, segundo_apellido=person.segundo_apellido, direccion=person.direccion, telefono=person.telefono, correo=person.correo, sangre=person.sangre, fecha_nacimiento=person.fecha_nacimiento, created_at=person.created_at, estatus=person.estatus)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

def update_person(db: Session, id: int, person: schemas.person.PersonUpdate):
    db_person = db.query(models.person.Person).filter(models.person.Person.id == id).first()
    if db_person:
        for var, value in vars(person).items():
            setattr(db_person, var, value) if value else None
        db.commit()
        db.refresh(db_person)
    return db_person

def delete_person(db: Session, id: int):
    db_person = db.query(models.person.Person).filter(models.person.Person.id == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person