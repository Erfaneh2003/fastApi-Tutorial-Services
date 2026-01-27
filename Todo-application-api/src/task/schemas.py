from pydantic import BaseModel , Field
from typing import Optional
from datetime import datetime




class TaskBaseSchemas (BaseModel):
    title : str = Field(..., max_length=200 , min_length=5 , description="The title of the task")
    description : Optional[str] = Field(..., max_length=500 , min_length=3 , description="The description of the task")
    is_completed : bool = Field(..., description="The status of the task")
    
    
    
class taskCreateSchemas (TaskBaseSchemas):
    pass



class taskUpdateSchemas (BaseModel):
    title : str = Field(..., max_length=200 , min_length=5 , description="The title of the task")
    description : Optional[str] = Field(..., max_length=500 , min_length=3 , description="The description of the task")
    is_completed : bool = Field(..., description="The status of the task")



class taskResponseSchemas (TaskBaseSchemas):
    id : int = Field(..., description="The unique ID of the task")
    created_date : datetime = Field(..., description="creation date and time of the object")
    updated_date : datetime = Field(..., description="last update date and time of the object")
    