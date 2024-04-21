import datetime
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Event:
    name: str
    start_time: str
    end_time: str
    context: str = "https://www.w3.org/ns/activitystreams"
    type: str = "Event"
    @property
    def start_datetime(self):
        return datetime.fromisoformat(self.start_time)
    @property
    def end_datetime(self):
        return datetime.fromisoformat(self.end_time)

@dataclass
class EventList:
    events: List[Event] = field(default_factory=list)
    def add_event(self, event: Event):
        self.events.append(event)
    def remove_event(self, event: Event):
        self.events.remove(event)
    def get_event(self, name: str) -> Optional[Event]:
        for event in self.events:
            if event.name == name:
                return event
        return None 