from fastapi import FastAPI
from command_handler import UserCommandHandler
from query_handler import UserQueryHandler

app = FastAPI()

command_handler = UserCommandHandler()
query_handler = UserQueryHandler()


@app.get("/")
def read_root():
    return {"message": "Welcome to the CQRS API!"}


@app.post("/users/")
def create_user(user_id: int, first_name: str, last_name: str, email: str):
    return command_handler.create_user(user_id, first_name, last_name, email)


@app.put("/users/{user_id}")
def update_email(user_id: int, new_email: str):
    return command_handler.update_user_email(user_id, new_email)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return query_handler.get_user(user_id)


@app.get("/users/")
def list_users():
    return query_handler.list_users()
