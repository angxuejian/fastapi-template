
from pydantic.generics import GenericModel
from pydantic import ConfigDict
from typing import Generic, TypeVar, Optional
from datetime import datetime

T = TypeVar("T")


class ResponseModel(GenericModel, Generic[T]):
    code: int = 0
    message: str = "success"
    data: Optional[T] = None

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S")
        }
    )

    @classmethod
    def success(cls, data: T = None, message: str = "success"):
        return cls(code=200, message=message, data=data)

    @classmethod
    def error(cls, message: str = "error", code: int = 500):
        return cls(code=code, message=message, data=None)