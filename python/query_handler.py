from sqlalchemy.orm import Session
from models import User


class UserQueryHandler:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id):
        user = self.db.query(User).filter_by(id=user_id).first()
        return {"id": user.id, "first name": user.first_name,
                "last name": user.last_name, "email": user.email} if user else {"error": "User not found!"}

    def list_users(self):
        users = self.db.query(User).all()
        return [{"id": user.id, "first name": user.first_name,
                 "last name": user.last_name, "email": user.email} for user in users]
