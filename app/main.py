from fastapi import FastAPI
from app.routers import subs, users, auth
from app import models
from app.database import engine

app = FastAPI()

app.include_router(subs.router)
app.include_router(users.router)
app.include_router(auth.router)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "This is the sub track api"}

