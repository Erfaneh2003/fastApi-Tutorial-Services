from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from app.database.database import get_db
from app import crud
from app.schemas.schemas import FoodUsageSchema
from typing import List
from app.crud.crud import get_food_usage

router = APIRouter()

@router.get("/food-usage/", response_model=List[FoodUsageSchema])
def get_food_usage_route(
    session_id: int = Query(..., description="Session ID"),
    start_date: date = Query(..., description="Start date (YYYY-MM-DD)"),
    end_date: date = Query(..., description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    return get_food_usage(db, session_id, start_date, end_date)
