from sqlalchemy.orm import Session
from .models import Issue
from sqlalchemy import func

def issue_stats(db: Session):
    open_issues = db.query(Issue).filter(Issue.status == "open").count()
    closed_issues = db.query(Issue).filter(Issue.status == "closed").count()

    avg_resolution = db.query(
        func.avg(Issue.closed_at - Issue.created_at)
    ).filter(Issue.closed_at.isnot(None)).scalar()

    return {
        "open": open_issues,
        "closed": closed_issues,
        "avg_resolution": str(avg_resolution)
    }
