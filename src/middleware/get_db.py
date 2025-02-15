from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import Annotated
from src.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]