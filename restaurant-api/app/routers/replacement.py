
from datetime import date
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import List 
from app.schemas.schemas import ReplacementFoodSchema
from app.database.database import get_db
from app.crud.crud import get_replacement_food
from typing import Optional

router = APIRouter()


# @router.get("/replacement-food", response_model=List[schemas.ReplacementFoodSchema])
# def get_replacement_food(sessionId: int, db: Session = Depends(database.get_db)):
#     replacement_food = crud.get_replacement_food(db, sessionId=sessionId)
#     return replacement_food


@router.get("/replacement-food/")
def  replacement_food_route(
    session_id: int,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return get_replacement_food(db, session_id, start_date, end_date)