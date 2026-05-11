from fastapi import APIRouter, Depends, HTTPException, status
from app import models, schemas, hashing
from app.database import db_dep


router = APIRouter()


@router.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user_in: schemas.UserCreate, db: db_dep):

    if db.query(models.User).filter(models.User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed = hashing.hash_password(user_in.password)
    
    user_data = user_in.model_dump(exclude={"password"}) 
    db_user = models.User(**user_data, hashed_password=hashed)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user