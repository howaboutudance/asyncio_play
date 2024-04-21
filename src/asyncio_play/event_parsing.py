"""Event parsing module."""
import json

from asyncio_play.schema import Event


def json_to_event_obj(event_json: str) -> Event:
    """Parse a json string into an Event object."""
    event_dict = json.loads(event_json)
    if (event_dict["type"] != "Event") or event_dict["@context"]!= "https://www.w3.org/ns/activitystreams":
        raise ValueError("The json is not an Event object.")

    return Event(
        name=event_dict["name"],
        start_time=event_dict["startTime"],
        end_time=event_dict["endTime"]
    )