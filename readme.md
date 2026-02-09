# Cloud-Based Issue Tracker

A production-style, containerized issue tracking backend built with **FastAPI**, **PostgreSQL**, and **Docker**.  
This project demonstrates backend API development, relational data modeling, containerization, and cloud-ready deployment practices.

---

## Features

- RESTful API for issue tracking
- User creation with hashed passwords
- Create, update, and close issues
- Issue analytics (open vs closed, average resolution time)
- PostgreSQL relational database
- Dockerized multi-container setup (API + DB)
- Designed for cloud deployment

---

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** Password hashing with bcrypt
- **Containerization:** Docker, Docker Compose
- **API Docs:** Swagger

---

## Project Structure

```
issue-tracker/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # DB connection & retry logic
│   ├── models.py        # SQLAlchemy models
│   ├── crud.py          # Database operations
│   ├── analytics.py     # Issue analytics queries
│   └── auth.py          # Password hashing utilities
├── tests/
│   └── test_basic.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```


---

## Running the Project Locally

### Prerequisites
- Docker Desktop (Windows / macOS / Linux)
- Docker Compose enabled

---

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/issue-tracker.git
cd issue-tracker
```
### Build and run containers
```
docker compose up --build
```
### Access the API
```
http://localhost:8000/docs
```
### API Endpoints

Create a user:
```
POST /users/
```

Create an issue:
```
POST /issues/
```

Close an issue:
```
POST /issues/{issue_id}/close
```

View Analytics:
    GET /analytics/
