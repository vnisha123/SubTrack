from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated 
from app import models,hashing,tokens
from app.routers.users import db_dep

router = APIRouter()
form_dep = Annotated[OAuth2PasswordRequestForm, Depends()]

@router.post("/login")
def login(db: db_dep, form_data: form_dep):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()

    if not user or not hashing.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Invalid Credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token = tokens.create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


