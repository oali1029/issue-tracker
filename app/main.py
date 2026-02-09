from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, crud, analytics
from .schemas import (
    UserCreate,
    UserResponse,
    IssueCreate,
    IssueResponse,
)

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud-Based Issue Tracker")


# Dependency: get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#User Endpoints

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user with a hashed password.
    """
    return crud.create_user(db, user.username, user.password)


#Issue Endpoints

@app.post("/issues/", response_model=IssueResponse)
def create_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    """
    Create a new issue associated with a user.
    """
    return crud.create_issue(
        db,
        title=issue.title,
        description=issue.description,
        priority=issue.priority,
        user_id=issue.owner_id,
    )


@app.post("/issues/{issue_id}/close", response_model=IssueResponse)
def close_issue(issue_id: int, db: Session = Depends(get_db)):
    """
    Close an issue and record the resolution timestamp.
    """
    return crud.close_issue(db, issue_id)


#Analytics Endpoint 

@app.get("/analytics/")
def get_analytics(db: Session = Depends(get_db)):
    """
    Return aggregated issue analytics.
    """
    return analytics.issue_stats(db)
