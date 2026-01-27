from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from app.database.database import get_db
from app import crud
from app.schemas.schemas import ReserveInfoSchema
from typing import List
from app.crud.crud import get_reserve_info


router = APIRouter()

@router.get("/reserve-info/", response_model=List[ReserveInfoSchema])
def reserve_info_route(
    session_id: int = Query(..., description="Session ID"),
    start_date: date = Query(..., description="Start date (YYYY-MM-DD)"),
    end_date: date = Query(..., description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    return get_reserve_info(db, session_id, start_date, end_date)
