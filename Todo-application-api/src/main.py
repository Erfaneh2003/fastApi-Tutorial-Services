

from fastapi import FastAPI , Depends , Cookie , Response , Request
from contextlib import asynccontextmanager
from src.task.routes import router as task_router
from src.users.routes import router as user_router  
from src.users.models import UserModel
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer


tags_metadata = [
    {
        "name": "tasks",
        "description": "Operations related to task management",
        "externalDocs": {
            "description": "More about tasks",
            "url": "https://exa"
        }
    }
]


@asynccontextmanager
async def lifespan (app: FastAPI):
    print ("application startup")
    yield
    print ("application shutdown")
    
    
app=FastAPI(
    title="todo application",
    description="a simple todo application built with fastapi and pydantic",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Erfaneh",
        "url": "http://example.com/contact/",
        "email": "erfaneh@example.com"  
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },      
    lifespan = lifespan ,   openapi_tags=tags_metadata  
    
    )

app.include_router(task_router , prefix="" )

app.include_router(user_router )


# from fastapi.security import APIKeyHeader

# header_schema = APIKeyHeader (name = "x-key")
# header_schema = APIKeyHeader (name = "x-key")
# query_schema = APIKeyHeader (name = "api_key")


# from fastapi.security import HTTPBasic , HTTPBasicCredentials

# security = HTTPBasic()
# security = HTTPBearer (scheme_name="token")

from src.auth.token_auth import get_authenticate_user



@app.get("/public")
def public_route():
    return {"message": "this is a public route "}

@app.get ("/private")
def private_route(user =  Depends (get_authenticate_user)):
    print (user.id)
    return {"message": "this is a private route "}


    
@app.post("/set-cookie")
def set_cookie(response: Response):
    response.set_cookie(key="test" , value="abcdef123456")
    return {"message": "cookie set"}


@app.get("/get-cookie")
def get_cookie(request : Request):
    print (request.__dict__)
    return {"message":"cookie has been get "}





#     print (credentials)
#     return {"message": "this is a private route "}

# @app.get ("/private")
# def private_route(api_key = Depends(query_schema)):
#     print (api_key)
#     return {"message": "this is a private route "}

# @app.get ("/private")
# def private_route(user : UserModel = Depends (get_authenticate_user)):
#     print (user)
#     return {"message": "this is a private route "}