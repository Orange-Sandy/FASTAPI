
# CRUD APPLICATION - FASTAPI


## Installation
Create Virtual Environment
```bash
 py -3 -m venv venv
```

Activate Virtual envirnment
```bash
 venv\scripts\activate
```

After activating the Virtual Environment install the Requirements by:
```bash
 pip install -r requirements.txt
```

## Database
Create a Table "users" in Database with the Fields as follows:

| Field             | Datatype                                                                |
| ----------------- | ------------------------------------------------------------------ |
| id            |   int(11)          |
| name          |   varchar(255)     |
| email         |   varchar(255)     |
| password      |   varchar(255)     |


## Run Code

To run the Application
```bash
 uvicorn main:app --reload
```

To Open Swagger Documentation - 
{url}/docs
```bash
 http://127.0.0.1:8000/docs
```