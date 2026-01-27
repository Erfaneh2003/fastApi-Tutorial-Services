from fastapi import HTTPException , status , Depends
from fastapi.security import HTTPBasic , HTTPBasicCredentials ,HTTPAuthorizationCredentials , HTTPBearer
from src.users.models import UserModel , TokenModel
from fastapi import FastAPI
from src.core.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import DecodeError, ExpiredSignatureError , InvalidSignatureError
from src.core.config import settings





security = HTTPBearer ()

def get_authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), 
    db: Session = Depends(get_db)
):
    token =credentials.credentials
    try:
        decode = jwt.decode(token , settings.JWT_SECRET_KEY , algorithms="HS256")
        user_id = decode.get("user_id" , None)
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="authentication Failed , user id not found",
            )
        if decode.get("type") != "access":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
            )
        if datetime.now () > datetime.fromtimestamp(decode.get("exp", 0)) :
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )
        user_obj = db.query(UserModel).filter_by(id=user_id).one()
        return user_obj
        
    
    except InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token signature",
        )
        
    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token decode error",
        )
    except  Exception as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="authentication Failed , {e}",
        )
                
    
      


def generate_access_token (uer_id:int , expire_in :int =60*5)-> str:
    now =datetime.utcnow()
    payload = {
        "user_id": uer_id,
        "iat": now,
        "exp": now + timedelta (seconds=expire_in),
        "type": "access"}
    return jwt.encode (payload , settings.JWT_SECRET_KEY , algorithm = "HS256")


def  generate_refresh_token (user_id:int , expire_in :int = 3600*24) -> str:
    now = datetime.utcnow()
    payload = {
        "user_id": user_id,
        "iat": now,
        "exp": now + timedelta (seconds=expire_in),
        "type": "refresh"}
    return jwt.encode (payload , settings.JWT_SECRET_KEY , algorithm = "HS256")




def decode_refresh_token (token ):
    try:
        decode = jwt.decode(token , settings.JWT_SECRET_KEY , algorithms="HS256")
        user_id = decode.get("user_id" , None)
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="authentication Failed , user id not found",
            )
        if decode.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type",
            )
        if datetime.now () > datetime.fromtimestamp(decode.get("exp", 0)) :
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )
        return user_id
    
    except InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token signature",
        )
        
    except DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token decode error",
        )
    except  Exception as e :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="authentication Failed , {e}",
        )
    