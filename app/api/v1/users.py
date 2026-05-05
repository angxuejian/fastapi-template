from fastapi import APIRouter, Form, UploadFile, File, Request, Depends
from app.api.deps import check_current_role

router = APIRouter()



@router.get('/', dependencies = [Depends(check_current_role('user:read'))])
def get_user(request: Request):
    # content-type: application/json
    print(request.state.user)
    return { "msg": "Hello uu" }

@router.post('/add', dependencies = [Depends(check_current_role('user:add'))])
def add_user(
    request: Request,
    name: str = Form(...),
    age: int = Form(...)
):
    # content-type: application/x-www-form-urlencoded
    print(request.state.user)
    return { "name": name, "age": age }


@router.post('/upload', dependencies = [Depends(check_current_role('user:upload'))])
def upload(
    request: Request,
    file: UploadFile = File(...)
):
    # content-type: multipart/form-data
    return { "filename": file.filename }

