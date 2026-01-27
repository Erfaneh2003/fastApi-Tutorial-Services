from datetime import date
from sqlalchemy.orm import Session
from app.models import models
from app.models.models import ReserveInfo

from typing import Optional


def get_restaurant_info(db: Session, session_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.RestaurantInfo).filter(
        models.RestaurantInfo.session_id == session_id
    ).offset(skip).limit(limit).all()


def get_reserve_info(db, session_id: int, start_date, end_date):
    results = (
        db.query(ReserveInfo)
        .filter(
            ReserveInfo.session_id == session_id,
            ReserveInfo.reserveDate >= start_date,
            ReserveInfo.reserveDate <= end_date
        )
        .all()
    )

    return [
        {
            "session_id": r.session_id,
            "resturantNo": r.resturantNo,
            "reserve_date": r.reserveDate,
            "reserve_count": 1
        }
        for r in results
    ]





def get_person_credit(db: Session, session_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.PersonCredit).filter(
        models.PersonCredit.session_id == session_id
    ).offset(skip).limit(limit).all()





def get_food_info(db: Session, session_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.FoodInfo).filter(
        models.FoodInfo.resturantNo == session_id
    ).offset(skip).limit(limit).all()


# -------------------------
def get_food_usage(db: Session, session_id: int, start_date: date, end_date: date):
    return db.query(models.FoodUsage).filter(
        models.FoodUsage.session_id == session_id,
        models.FoodUsage.usageDate.between(start_date, end_date)
    ).all()




def get_replacement_food(
    db: Session, 
    session_id: int, 
    start_date: Optional[date] = None, 
    end_date: Optional[date] = None
):
    query = db.query(models.ReplacementFood).filter(
        models.ReplacementFood.session_id == session_id
    )

    if start_date:
        query = query.filter(models.ReplacementFood.replacement_date >= start_date)
    if end_date:
        query = query.filter(models.ReplacementFood.replacement_date <= end_date)

    return query.all()







def get_restaurant_range_oclock(db: Session, session_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.ResturantRangeOclock).filter(
        models.ResturantRangeOclock.session_id == session_id
    ).offset(skip).limit(limit).all()
