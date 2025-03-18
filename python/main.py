from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from command_handler import UserCommandHandler
from query_handler import UserQueryHandler

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the CQRS API!"}


@app.post("/users/")
def create_user(user_id: int, first_name: str, last_name: str, email: str, db: Session = Depends(get_db)):
    try:
        handler = UserCommandHandler(db)
        return handler.create_user(user_id, first_name, last_name, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/users/{user_id}")
def update_email(user_id: int, new_email: str, db: Session = Depends(get_db)):
    try:
        handler = UserCommandHandler(db)
        return handler.update_user_email(user_id, new_email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    handler = UserQueryHandler(db)
    return handler.get_user(user_id)


@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    handler = UserQueryHandler(db)
    return handler.list_users()
