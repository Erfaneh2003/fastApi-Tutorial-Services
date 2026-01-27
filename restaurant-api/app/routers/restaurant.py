from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.crud.crud import get_restaurant_info as crud_get_restaurant_info
from app.schemas.schemas import RestaurantInfoSchema
from app.database.database import get_db

router = APIRouter()

@router.get("/ResturantInfo/", response_model=List[RestaurantInfoSchema])
def restaurant_info_route(session_id: int, db: Session = Depends(get_db)):
    restaurant_info = crud_get_restaurant_info(db, session_id)
    return restaurant_info
