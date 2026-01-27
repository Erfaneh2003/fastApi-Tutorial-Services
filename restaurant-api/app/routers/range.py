from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app import crud
from app.schemas.schemas import ResturantRangeOclockSchema
from typing import List ,Optional 
from app.crud.crud import get_restaurant_range_oclock
from datetime import date

router = APIRouter()

@router.get("/resturant-range-oclock/", response_model=List[ResturantRangeOclockSchema])
def get_range_oclock_route(
    session_id: int = Query(..., description="Session ID"),
    db: Session = Depends(get_db)
):
    return get_restaurant_range_oclock(db, session_id)
