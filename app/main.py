from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, crud, analytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    return crud.create_user(db, username, password)

@app.post("/issues/")
def create_issue(title: str, description: str, priority: str, user_id: int, db: Session = Depends(get_db)):
    return crud.create_issue(db, title, description, priority, user_id)

@app.post("/issues/{issue_id}/close")
def close_issue(issue_id: int, db: Session = Depends(get_db)):
    return crud.close_issue(db, issue_id)

@app.get("/analytics/")
def get_analytics(db: Session = Depends(get_db)):
    return analytics.issue_stats(db)
