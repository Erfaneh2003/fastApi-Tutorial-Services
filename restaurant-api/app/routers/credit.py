from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app import crud
from app.schemas.schemas import PersonCreditSchema
from typing import List
from app.crud.crud import get_person_credit

router = APIRouter()

@router.get("/person-credit/", response_model=List[PersonCreditSchema])
def get_person_credit_router(
    session_id: int = Query(..., description="Session ID"),
    skip: int = Query(0),
    limit: int = Query(100),
    db: Session = Depends(get_db)
):
    return get_person_credit(db, session_id, skip, limit)
