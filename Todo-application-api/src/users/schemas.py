from pydantic import BaseModel , Field ,field_validator
from typing import Optional
from datetime import datetime



class UserlogSchema (BaseModel):
    username : str = Field(... , min_length=3 , max_length=50 , description="The username of the user")
    password : str = Field(... , min_length=6 , max_length=100 , description="The password of the user")        
    
    
    
class userRegisterSchema (BaseModel):
    username : str = Field(... , min_length=3 , max_length=50 , description="The username of the user")
    password : str = Field(... , min_length=6 , max_length=100 , description="The password of the user")        
    password_confirm : str = Field(... , min_length=6 , max_length=100 , description="The password confirmation of the user")
    
    @field_validator("password_confirm")
    def check_passwords_match(cls , password_confirm , validation):
        if  not  (password_confirm ==validation.data.get("password")):  
            raise ValueError("Passwords do not match")
        return password_confirm
    
    
class UserrefreshTokenSchema (BaseModel):
   token : str = Field(..., description="The refresh token of the user")