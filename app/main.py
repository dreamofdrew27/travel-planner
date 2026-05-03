from fastapi import FastAPI
from .database import engine, Base
from .routers import projects

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Travel Planner API"}

app.include_router(projects.router)
