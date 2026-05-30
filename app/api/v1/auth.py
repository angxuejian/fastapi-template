
from fastapi import APIRouter, Form, HTTPException
from app.core.security import create_access_token

router = APIRouter()


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # 模拟账号
    if username != "admin" or password != "123456":
        raise HTTPException(status_code=401, detail="access error")

    token = create_access_token({ "sub": username, "role": 'admin' })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

# @router.post("/logout")



@router.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    
    print(f"register: {username}, {password}")

    return {
        "message": "registration successful"
    }
