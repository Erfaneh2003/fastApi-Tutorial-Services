from fastapi import APIRouter , HTTPException , status , Depends ,  Path , Query , Body 
from starlette.responses import JSONResponse
from fastapi.responses import JSONResponse
from src.task.schemas import *
from src.task.models import TaskModel
from src.users.models import UserModel
from sqlalchemy.orm import Session 
from src.core.database import get_db
from typing import List 
from src.auth.jwt_auth import get_authenticate_user

router = APIRouter(tags=["tasks"])




@router.get ("/tasks/" , response_model=List[taskResponseSchemas])
async def retrieve_tasks_list(
    completed:bool = Query (None , description="filter tasks based on completion status") ,
    limit:int = Query (10 , gt=0 , le=100 , description="limiting the number of items to retrieve") ,
    offset:int = Query (0 , ge=0 , description="use for paginating based on passed items  ") ,
    db : Session = Depends (get_db),
    user : UserModel = Depends (get_authenticate_user)):
    query = db.query(TaskModel).filter_by(user_id=user.id)
    if completed is not None:
        query = query.filter_by(is_completed=completed)
    return query.offset(offset).limit(limit).all()


@router.get("/tasks/{task_id}", response_model=taskResponseSchemas)
async def retrieve_tasks_detail(task_id: int = Path (..., gt=0) , db: Session = Depends (get_db) ,user : UserModel = Depends (get_authenticate_user)):
    task_obj = db.query(TaskModel).filter_by(user_id=user.id , id=task_id).first()
    if not task_obj:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail=f"task with id {task_id} not found")
    return task_obj


@router.post ("/tasks/", status_code=status.HTTP_201_CREATED , response_model=taskResponseSchemas)
async def create_task(request: taskCreateSchemas, db: Session = Depends (get_db),user : UserModel = Depends (get_authenticate_user)):
    # print(request.model_dump())
    data=request.model_dump()
    data.update({"user_id":user.id})
    task_obj = TaskModel(**data)
    db.add(task_obj)
    db.commit()
    db.refresh(task_obj)
    return task_obj

@router.put ("/tasks/{task_id}" , response_model=taskResponseSchemas)
async def update_task(request:taskUpdateSchemas, task_id: int = Path (..., gt=0), db: Session = Depends (get_db)):
    task_obj = db.query(TaskModel).filter_by(id=task_id).first()
    if not task_obj:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail=f"task with id {task_id} not found")
    
    for field , value in request.model_dump(exclude_unset=True).items():
        setattr (task_obj , field , value)
        
    db.commit()
    db.refresh(task_obj)
    
    return task_obj
    


@router.delete ("/tasks/{task_id}" , status_code=status.HTTP_204_NO_CONTENT)
async def delete_task (task_id: int = Path (..., gt=0) , db: Session = Depends (get_db),user : UserModel = Depends (get_authenticate_user)):
    task_obj = db.query(TaskModel).filter_by(user_id=user.id ,id=task_id).first()
    if not task_obj:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND , detail=f"task with id {task_id} not found")
    db.delete (task_obj)    
    db.commit()
    


