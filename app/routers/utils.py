from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated 
from app import models,hashing,tokens
from app.database import get_db
from app.database import db_dep

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dep):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    user_id = tokens.verify_access_token(token)
    if user_id is None:
        raise credentials_exception
    
    user = db.query(models.User).filter(models.User.id == int(user_id)).first()
    if user is None:
        raise credentials_exception
        
    return user