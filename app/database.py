from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@db:5432/issues"
)

# Retry logic for DB startup
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        break
    except OperationalError:
        print("Database not ready, retrying...")
        time.sleep(2)
else:
    raise Exception("Database never became available")

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
