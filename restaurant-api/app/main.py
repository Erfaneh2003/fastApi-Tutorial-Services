from datetime import date
from fastapi import FastAPI
from app.routers import restaurant, reserve, credit, food, range,replacement
from app.database.mock_data import init_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()


init_db()


app.include_router(restaurant.router, prefix="/attendance/api/v1/restaurants", tags=["Restaurants"])
app.include_router(reserve.router, prefix="/attendance/api/v1/restaurants", tags=["Reserve"])
app.include_router(credit.router, prefix="/attendance/api/v1/restaurants", tags=["Credit"])
app.include_router(food.router, prefix="/attendance/api/v1/restaurants", tags=["Food"])
app.include_router(replacement.router, prefix="/attendance/api/v1/restaurants", tags=["Replacement"])
app.include_router(range.router, prefix="/attendance/api/v1/restaurants", tags=["Range"])



app.mount("/static", StaticFiles(directory="static"), name="static")