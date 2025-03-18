from sqlalchemy.orm import Session
from models import User


class UserCommandHandler:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_id, first_name, last_name, email):
        if self.db.query(User).filter_by(id=user_id).first():
            raise ValueError("User already exists!")
        new_user = User(id=user_id, first_name=first_name, last_name=last_name, email=email)
        self.db.add(new_user)
        self.db.commit()
        return {"message": f"User {first_name} created successfully!"}

    def update_user_email(self, user_id, new_email):
        user = self.db.query(User).filter_by(id=user_id).first()
        if not user:
            raise ValueError("User not found!")
        user.email = new_email
        self.db.commit()
        return {"message": f"User {user_id} email updated!"}
