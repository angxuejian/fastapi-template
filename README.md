# FastAPI Template

A personal FastAPI template project for building structured and scalable backend services.

<!-- 1、source pyenv/bin/activate | deactivate -->
<!-- 2、uvicorn app.main:app --reload -->
<!-- 3、pip freeze > requirements.txt -->
<!-- 4、python3 -c "import secrets; print(secrets.token_urlsafe(32))" -->
<!-- docker compose -f dev.yml --env-file .env.example up -d --build -->
<!-- docker compose -f dev.yml down -v -->


<!-- http://127.0.0.1:8000/docs -->
<!-- http://127.0.0.1:8000/redoc -->

<!-- ```
from pydantic import BaseModel, Field, EmailStr, HttpUrl, field_validator, model_validator
from typing import List, Optional
from enum import Enum
from datetime import datetime
from uuid import UUID


class Role(str, Enum):
    admin = 'admin'
    user = 'user'

class Profile(BaseModel):
    bio: str

class User(BaseModel):
    uid: UUID
    name: str = Field(min_length=3)
    age: int = Field(ge=0) # >= 0
    email: EmailStr
    website: HttpUrl
    tags: List[str]
    role: Role
    profile: Profile
    address: Optional[str] = None
    phone_number: int = Field(min_length=11, alias="phonenumber")
    created_at: datetime
    password: str
    confirm_password: str

    @field_validator("age")
    def check_age(cls, v):
        if v < 18:
            raise ValueError("must be >= 18")
        return v

    @model_validator(mode="after")
    def check_password(cls, v):
        if v.password != v.confirm_password:
            raise ValueError("password mismatch")
        return v

``` -->