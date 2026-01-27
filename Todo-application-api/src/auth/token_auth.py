from fastapi import HTTPException , status , Depends
from fastapi.security import HTTPBasic , HTTPBasicCredentials ,HTTPAuthorizationCredentials , HTTPBearer
from src.users.models import UserModel , TokenModel
from fastapi import FastAPI
from src.core.database import get_db
from sqlalchemy.orm import Session




security = HTTPBearer (scheme_name="token")

def get_authenticate_user(
    credentials: HTTPAuthorizationCredentials = Depends(security), 
    db: Session = Depends(get_db)):
    token_obj = db.query (TokenModel).filter_by(token=credentials.credentials).one_or_none()
    if not token_obj:
          raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "authentication Failed",
           
        )
        
    
        
        
    return token_obj.user