from fastapi import APIRouter,Depends,HTTPException,status
from app.schemas import SubCreate,SubResponse,SubUpdate
from app.routers.utils import get_current_user
from app import models
from app.database import db_dep
router = APIRouter()

@router.post("/subscriptions",response_model=SubResponse)
async def create_sub( sub: SubCreate, db:db_dep,current_user: models.User = Depends(get_current_user)):

    sub_data = sub.model_dump()

    new_sub = models.Sub(**sub_data,user_id=current_user.id)

    db.add(new_sub)
    db.commit()
    db.refresh(new_sub)
    return new_sub

@router.get("/subscriptions", response_model=list[SubResponse])
async def get_all_user_subscriptions(db: db_dep,current_user: models.User = Depends(get_current_user)):
    
    subscriptions = db.query(models.Sub).filter(models.Sub.user_id == current_user.id).all()
    return subscriptions


@router.get("/subscriptions/{sub_id}", response_model=SubResponse)
async def get_sub(sub_id: int, db: db_dep, current_user: models.User = Depends(get_current_user)):

    sub = db.query(models.Sub).filter(models.Sub.id == sub_id).first()
    
    if sub is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subscription not found"
        )
    
    if sub.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You are not authorized to view this subscription"
        )
        
    return sub



@router.put("/subscriptions/{sub_id}", response_model=SubResponse)
async def update_sub(sub_id: int,sub_update: SubUpdate, db: db_dep,current_user: models.User = Depends(get_current_user)):
   
    sub = db.query(models.Sub).filter(models.Sub.id == sub_id).first()
    
    if sub is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subscription not found"
        )
        
    if sub.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You are not authorized to modify this subscription"
        )
  
    update_data = sub_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(sub, key, value)
        
    db.commit()
    db.refresh(sub)
    return sub


@router.delete("/subscriptions/{sub_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sub(
    sub_id: int,
    db: db_dep,
    current_user: models.User = Depends(get_current_user)
):
   
    sub = db.query(models.Sub).filter(models.Sub.id == sub_id).first()
    
  
    if sub is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Subscription not found"
        )
        
  
    if sub.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="You are not authorized to delete this subscription"
        )
    
  
    db.delete(sub)
    db.commit()
    
    return None