
from fastapi import Depends, Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token

security = HTTPBearer()

def get_current_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = payload.get("sub")
    role = payload.get("role")
    if not user:
        raise HTTPException(status_code=401, detail="Token error")

    # 👇 存入上下文
    request.state.user = user
    request.state.role = role

    return user


def check_current_role(permission: str):
    def checker(request: Request):
        role = getattr(request.state, "role", None)
        if not role:
            raise HTTPException(status_code=403, detail="No permission")

        perms = { 'admin': ['user:read'] }.get(role, [])

        if permission not in perms:
             raise HTTPException(status_code=403, detail="No permission")
    
    return checker