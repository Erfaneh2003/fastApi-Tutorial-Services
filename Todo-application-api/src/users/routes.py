from fastapi import APIRouter , HTTPException , status , Depends ,  Path , Query , Body , Cookie , Response 
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse  
from src.users.schemas import *
from src.users.models import UserModel , TokenModel       
from sqlalchemy.orm import Session
from src.core.database import get_db
from typing import List
import secrets
from src.auth.jwt_auth import generate_access_token , generate_refresh_token , decode_refresh_token



router = APIRouter(tags=["users"] , prefix="/users")

def generate_token (length = 32):
    return secrets.token_hex (length)




@router.post ("/login")
async def user_login (request: UserlogSchema , db : Session = Depends (get_db)):
    user_obj= db.query(UserModel).filter_by(username=request.username).first()
    if not user_obj:
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST , detail="user does not exist")
    if not user_obj.verify_password(request.password):
        raise HTTPException (status_code=status.HTTP_400_BAD_REQUEST, detail="password is incorrect")
    # token_obj = TokenModel(user_id = user_obj.id , token = generate_token())
    # db.add(token_obj)
    # db.commit()
    # db.refresh(token_obj)
    access_token = generate_access_token(user_obj.id)
    Refresh_token = generate_refresh_token(user_obj.id)
    return JSONResponse(content={"detail":"logged in successfully" , "access_token": access_token, "refresh_token": Refresh_token})


@router.post("/register")
async def user_register(request:userRegisterSchema  , db :Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username=request.username).first():
        raise HTTPException (status_code=status.HTTP_409_CONFLICT , detail="Username already exists"  )
    user_obj = UserModel(username=request.username.lower())
    user_obj.set_password(request.password)
    db.add(user_obj)
    db.commit() 
    return JSONResponse (status_code=status.HTTP_201_CREATED , content={"message":"User registered successfully"})



@router.post("/refresh-token")
async def user_refresh_token(request:UserrefreshTokenSchema , db :Session = Depends (get_db)):
    user_id = decode_refresh_token(request.token )
    access_token = generate_access_token(user_id)
    return JSONResponse(content={"access_token":access_token})
    
    
