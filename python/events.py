class UserCreatedEvent:
    def __init__(self, user_id, first_name, last_name, email):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }


class UserEmailUpdatedEvent:
    def __init__(self, user_id, new_email):
        self.user_id = user_id
        self.new_email = new_email

    def to_dict(self):
        return {"user_id": self.user_id, "new_email": self.new_email}
