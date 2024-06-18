from fastapi import APIRouter

user = APIRouter()

@user.get("/users")

def helloWorld():
    return "Hola 9°B"

@user.get("/prueba")

def sayHello():
    return "Hello"