from sqlalchemy import Column, Integer, String, Boolean , func, Integer, DateTime , ForeignKey 
from src.core.database import Base
from sqlalchemy.orm import relationship

# class UserModel (Base):
#     __tablename__ = "users"

#     id = Column (Integer, primary_key = True, autoincrement = True)
#     username = Column (String(250), nullable = False)
#     password = Column (String, nullable = False)
    
#     is_active = Column (Boolean, default = False)\
        
#     created_date = Column (DateTime, server_default=func.now())
#     updated_date = Column (DateTime, server_default=func.now(), onupdate=func.now())
    
#     task = relationship ("taskModel" , back_populates="user")
    
    
    
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 


class UserModel (Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key = True, autoincrement = True)
    username = Column (String(250), nullable = False, unique=True)
    password = Column (String, nullable = False)
    
    is_active = Column (Boolean, default = True)
        
    created_date = Column (DateTime, server_default=func.now())
    updated_date = Column (DateTime, server_default=func.now(), onupdate=func.now())
    
    task = relationship ("TaskModel" , back_populates="user")
    
    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.password)


    def set_password(self, plain_text: str) -> None:
        self.password = self.hash_password(plain_text)
        
        
        
class TokenModel(Base):
    __tablename__ = "token "

    id = Column (Integer, primary_key = True, autoincrement = True)
    user_id = Column (Integer , ForeignKey("users.id"))
    token = Column (String, nullable = False, unique=True)
    created_date = Column (DateTime, server_default=func.now())
    user = relationship ("UserModel", uselist = False )
    