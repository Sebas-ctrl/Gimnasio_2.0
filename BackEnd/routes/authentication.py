from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import config.db, schemas.authentication, models.users, crud.authentication
import jwt

models.users.Base.metadata.create_all(bind=config.db.engine)
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

auth = APIRouter()

@auth.post("/auth")
async def generate_jwt(user: schemas.authentication.AuthCreate, db: Session = Depends(get_db)):
    db_user = crud.authentication.get_user(db, user=user)
    if db_user:
        encoded_jwt = jwt.encode({
            "email": user.correo, 
            "pass": user.contrasena
        },  
        "mysupersecret", 
        algorithm="HS256")
        
        return {"token": encoded_jwt}
        
    raise HTTPException(status_code=400, detail="El usuario no existe")