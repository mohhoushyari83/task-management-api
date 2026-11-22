from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Task Management API",
    description="A simple API for managing tasks",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Task Management API"
    }
