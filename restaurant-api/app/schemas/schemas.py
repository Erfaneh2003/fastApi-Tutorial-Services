
from datetime import date, time
from pydantic import BaseModel , ConfigDict
from typing import List, Optional
from pydantic import BaseModel
from datetime import date

class RestaurantInfoSchema(BaseModel):
    session_id: int
    resturantNo: int
    resturantName: str
    active: bool
    foodTerm: int
    resturantLocation: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)



class ReserveInfoSchema(BaseModel):
    session_id: int
    resturantNo: int
    reserve_date: date
    reserve_count: int

    class Config:
        from_attributes = True



class PersonCreditSchema(BaseModel):
    session_id: int
    resturantNo: int
    credit: int

    model_config = ConfigDict(from_attributes=True)


class FoodInfoSchema(BaseModel):
    foodID: int
    foodName: str
    resturantNo: int

    model_config = ConfigDict(from_attributes=True)



class FoodUsageSchema(BaseModel):
    session_id: int
    foodID: int
    usageDate: date

    model_config = ConfigDict(from_attributes=True)




class ReplacementFoodSchema(BaseModel):
    session_id: int
    replacement_date: date
    foodID: int
    replacedFoodID: int
    food_name: Optional[str] = None 

    model_config = ConfigDict(from_attributes=True)

class ResturantRangeOclockSchema(BaseModel):
    session_id: int
    resturantNo: int
    startTime : time
    endTime : time
    
    model_config = ConfigDict(from_attributes=True)

