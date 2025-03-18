from database import SessionLocal, engine, Base
from models import Event

Base.metadata.create_all(bind=engine)


class EventStore:
    def __init__(self):
        self.db = SessionLocal()

    def add_event(self, event_type, data):
        event = Event(event_type=event_type, data=data)
        self.db.add(event)
        self.db.commit()

    def get_events(self):
        return self.db.query(Event).all()

    def get_all_events(self):
        events = self.db.query(Event).all()
        return [{"id": event.id, "type": event.event_type, "data": event.data} for event in events]
