
from pydantic import BaseModel, ConfigDict
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    created_time: datetime
    
    model_config = ConfigDict(
        from_attributes=True  # ⭐️ 关键
    )