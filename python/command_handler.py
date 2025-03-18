from events import UserCreatedEvent, UserEmailUpdatedEvent
from event_store import EventStore


class UserCommandHandler:
    def __init__(self):
        self.event_store = EventStore()

    def create_user(self, user_id, first_name, last_name, email):
        event = UserCreatedEvent(user_id, first_name, last_name, email)
        self.event_store.add_event("UserCreated", event.to_dict())
        return {"message": f"User {first_name} {last_name} created successfully!"}

    def update_user_email(self, user_id, new_email):
        event = UserEmailUpdatedEvent(user_id, new_email)
        self.event_store.add_event("UserEmailUpdated", event.to_dict())
        return {"message": f"User {user_id} email updated!"}
