from fastapi import APIRouter, Form, UploadFile, File, Request, Depends
from app.api.deps import check_current_role, get_db
from app.schemas.base import ResponseModel
from app.schemas.users import UserResponse
from app.services.users import user_add

router = APIRouter()


# 
@router.get('/get', response_model=ResponseModel, dependencies = [Depends(check_current_role('user:read'))])
def get_user(request: Request, name: str | None = None):
    # content-type: application/json

    print(request.state.user)
    return ResponseModel.success('Hello uu')

@router.post('/add', response_model=ResponseModel[UserResponse], dependencies = [Depends(check_current_role('user:add'))])
def add_user(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    db = Depends(get_db)
):
    # content-type: application/x-www-form-urlencoded

    user = user_add(db=db, name=name, age=age)
    
    return ResponseModel.success(user)


@router.post('/upload', dependencies = [Depends(check_current_role('user:upload'))])
def upload(
    request: Request,
    file: UploadFile = File(...)
):
    # content-type: multipart/form-data
    return { "filename": file.filename }

