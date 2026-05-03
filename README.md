Travel Planner API

A simple REST API for managing travel projects and planning places to visit.
Built with FastAPI and SQLite.

---

Features

- Create travel projects
- Get all projects
- Get project by ID
- SQLite database integration
- Swagger UI for testing API

---

Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

How to run

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Start the server
```bash
uvicorn app.main:app --reload
```
3. Open API documentation
http://127.0.0.1:8000/docs

4. Test API
   
Use Swagger UI to:
-Create a project
-Get all projects
-Get project by ID
