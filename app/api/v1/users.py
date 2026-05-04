from fastapi import APIRouter, Form, UploadFile, File

router = APIRouter()



@router.get('/')
def get_user():
    # content-type: application/json

    return { "msg": "Hello uu" }

@router.post('/add')
def add_user(
    name: str = Form(...),
    age: int = Form(...)
):
    # content-type: application/x-www-form-urlencoded

    return { "name": name, "age": age }


@router.post('/upload')
def upload(
    file: UploadFile = File(...)
):
    # content-type: multipart/form-data

    return { "filename": file.filename }

