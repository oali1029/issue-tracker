from sqlalchemy.orm import Session
from . import models, auth
from datetime import datetime

def create_user(db: Session, username: str, password: str):
    user = models.User(
        username=username,
        password_hash=auth.hash_password(password)
    )
    db.add(user)
    db.commit()
    return user

def create_issue(db: Session, title, description, priority, user_id):
    issue = models.Issue(
        title=title,
        description=description,
        priority=priority,
        owner_id=user_id
    )
    db.add(issue)
    db.commit()
    return issue

def close_issue(db: Session, issue_id: int):
    issue = db.query(models.Issue).get(issue_id)
    issue.status = "closed"
    issue.closed_at = datetime.utcnow()
    db.commit()
    return issue
