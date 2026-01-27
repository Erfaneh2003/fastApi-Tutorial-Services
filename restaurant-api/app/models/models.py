# file: app/models/models.py
from datetime import date, time
from sqlalchemy import Column, Integer, String, Boolean, Date
from app.database.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Date, DateTime , Time





class RestaurantInfo(Base):
    __tablename__ = "restaurant_info"
    session_id = Column(Integer, primary_key=True, index=True)
    resturantNo = Column(Integer, nullable=False)
    resturantName = Column(String, nullable=False)
    active = Column(Boolean, default=True)
    foodTerm = Column(Integer, nullable=True)
    resturantLocation = Column(String, nullable=True)

class ReserveInfo(Base):
    __tablename__ = "reserve_info"
    personID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(Integer, nullable=False)
    resturantNo = Column(Integer, nullable=False)
    reserveDate = Column(Date, nullable=False)
    reserveTime = Column(Time, nullable=True)

class PersonCredit(Base):
    __tablename__ = "person_credit"
    session_id = Column(Integer, primary_key=True)
    resturantNo = Column(Integer, nullable=False)
    credit = Column(Integer, default=0)

class FoodInfo(Base):
    __tablename__ = "food_info"
    foodID = Column(Integer, primary_key=True)
    foodName = Column(String, nullable=False)
    resturantNo = Column(Integer, nullable=False)

class FoodUsage(Base):
    __tablename__ = "food_usage"
    session_id = Column(Integer, primary_key=True)
    foodID= Column(Integer, primary_key=True)
    usageDate = Column(Date, primary_key=True)
    
    
    
class ReplacementFood(Base):
    __tablename__ = "replacement_food"
    session_id = Column(Integer, primary_key=True)
    replacement_date = Column(Date, nullable=False)
    food_name = Column(String, nullable=False)
    foodID = Column(Integer, nullable=False)
    
    
class ResturantRangeOclock(Base):
    __tablename__ = "resturant_range_oclock"
    session_id = Column(Integer, primary_key=True)
    resturantNo = Column(Integer, nullable=False)
    startTime = Column(Time, nullable=False)
    endTime = Column(Time, nullable=False)
