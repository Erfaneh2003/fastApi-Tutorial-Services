# file: app/database/mock_data.py
from datetime import date, time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.database import Base
from app.models.models import (
    RestaurantInfo,
    ReserveInfo,
    PersonCredit,
    FoodInfo,
    FoodUsage,
    ReplacementFood,
    ResturantRangeOclock
)


def init_db():
  
    engine = create_engine("sqlite:///test_restaurant.db", echo=True)
    SessionLocal = sessionmaker(bind=engine)
    

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # RestaurantInfo
    db.add_all([
        RestaurantInfo(session_id=1455, resturantNo=1, resturantName="Resto A", active=True, foodTerm=1, resturantLocation="Tehran"),
        RestaurantInfo(session_id=1456, resturantNo=2, resturantName="Resto B", active=True, foodTerm=2, resturantLocation="Shiraz")
    ])

    # ReserveInfo
    db.add_all([
        ReserveInfo(session_id=1455, resturantNo=1, reserveDate=date(2026,1,3), reserveTime=time(12,0)),
        ReserveInfo(session_id=1456, resturantNo=2, reserveDate=date(2026,1,4), reserveTime=time(18,0))
    ])

    # PersonCredit
    db.add_all([
        PersonCredit(session_id=1455, resturantNo=1, credit=100),
        PersonCredit(session_id=1456, resturantNo=2, credit=50)
    ])

    # FoodInfo
    db.add_all([
        FoodInfo(foodID=1, foodName="Pizza", resturantNo=1),
        FoodInfo(foodID=2, foodName="Burger", resturantNo=1),
        FoodInfo(foodID=3, foodName="Pasta", resturantNo=2)
    ])

    # FoodUsage
    db.add_all([
        FoodUsage(session_id=1455, foodID=1, usageDate=date(2026,1,1)),
        FoodUsage(session_id=1455, foodID=2, usageDate=date(2026,1,2)),
        FoodUsage(session_id=1456, foodID=3, usageDate=date(2026,1,3))
    ])

    # # ReplacementFood
    db.add_all([
        ReplacementFood(session_id=1455, foodID=1, replacement_date=date(2026, 1, 1), food_name="Pizza replaced by Burger"),
        ReplacementFood(session_id=1456, foodID=2, replacement_date=date(2026, 1, 2), food_name="Burger replaced by Pasta")
    ])

    # ResturantRangeOclock
    db.add_all([
        ResturantRangeOclock(session_id=1455, resturantNo=1, startTime=time(8,0), endTime=time(14,0)),
        ResturantRangeOclock(session_id=1456, resturantNo=2, startTime=time(17,0), endTime=time(22,0))
    ])

    db.commit()
    db.close()

    print("Mock data inserted successfully!")
