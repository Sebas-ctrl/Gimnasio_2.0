import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user):
    return db.query(models.users.User).filter(models.users.User.Correo_Electronico == user.correo, models.users.User.Contrasena == user.contrasena).first()
