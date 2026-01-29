# FastAPI Mock Enterprise App (System Under Test)

This portfolio uses an external FastAPI mock enterprise application as its
System Under Test (SUT).

## Features
- Token-based authentication (HTTP Bearer)
- Devices CRUD API
- Swagger UI enabled
- In-memory mock data store

## How to Run the SUT

```bash
uvicorn app.main:app --port 8080 --reload
