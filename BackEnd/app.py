from fastapi import FastAPI
from routes.user import user
from routes.personas import persona

app = FastAPI()
app.include_router(user)
app.include_router(persona)

print("¡Hello! Welcome to my Backend") 