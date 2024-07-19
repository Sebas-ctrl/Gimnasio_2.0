from fastapi import FastAPI
from routes.user import user
from routes.personas import persona
from routes.roles import rol
from routes.usuarios_roles import usuario_rol
from routes.authentication import auth

app = FastAPI()
app.include_router(user)
app.include_router(persona)
app.include_router(rol)
app.include_router(usuario_rol)
app.include_router(auth)

print("¡Hello! Welcome to my Backend")