from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.crud import user as user_crud
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/", response_model=list[user_schema.UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_crud.get_users(db)
