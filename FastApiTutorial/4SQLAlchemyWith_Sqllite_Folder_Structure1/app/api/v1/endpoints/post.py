from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import post as post_schema
from app.crud import post as post_crud
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=post_schema.PostResponse)
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db)):
    return post_crud.create_post(db, post, user_id=1)  # just for demo, fixed user_id

@router.get("/", response_model=list[post_schema.PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return post_crud.get_posts(db)
