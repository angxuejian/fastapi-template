
from sqlalchemy.orm import Session
from app.models.users import Users

def user_add(db: Session, name: str, age: int):

    user = Users(name=name, age=age)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user