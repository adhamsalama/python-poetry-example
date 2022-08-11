from fastapi import FastAPI
from rest_api.routes import index
from rest_api.routes import todo

app = FastAPI()

app.include_router(index.router)
app.include_router(todo.router, prefix="/todos")
