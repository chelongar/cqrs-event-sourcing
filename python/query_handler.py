from event_store import EventStore
from events import UserCreatedEvent, UserEmailUpdatedEvent


class UserQueryHandler:
    def __init__(self):
        self.event_store = EventStore()

    def get_user(self, user_id):
        user_data = {}
        for event in self.event_store.get_events():
            event_data = event.data

            # Ensure old events without first_name & last_name don't cause errors
            if event.event_type == "UserCreated" and event_data["user_id"] == user_id:
                user_data = {
                    "id": event_data["user_id"],
                    "first_name": event_data.get("first_name", "N/A"),  # Default to "N/A" if missing
                    "last_name": event_data.get("last_name", "N/A"),  # Default to "N/A" if missing
                    "email": event_data["email"]
                }
            elif event.event_type == "UserEmailUpdated" and event_data["user_id"] == user_id:
                user_data["email"] = event_data["new_email"]

        return user_data if user_data else {"error": "User not found!"}

    def list_users(self):
        users = {}
        for event in self.event_store.get_events():
            event_data = event.data

            if event.event_type == "UserCreated":
                users[event_data["user_id"]] = {
                    "id": event_data["user_id"],
                    "first_name": event_data.get("first_name", "N/A"),  # Handle missing fields
                    "last_name": event_data.get("last_name", "N/A"),
                    "email": event_data["email"]
                }
            elif event.event_type == "UserEmailUpdated":
                users[event_data["user_id"]]["email"] = event_data["new_email"]

        return list(users.values())
