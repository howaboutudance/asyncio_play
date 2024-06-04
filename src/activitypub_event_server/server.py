import logging

from activitypub_event_server.protos import EventServiceServicer, event_core

_log = logging.getLogger(__name__)


class EventServiceService(EventServiceServicer):
    """Event service servicer."""

    def GetEvent(self, request: event_core.GetEventRequest, context):
        """Get event."""
        _log.info("Get event request: %s", request)
        return event_core.GetEventResponse(
            event=event_core.Event(
                event_id=request.event_id,
                name="Event 1",
            )
        )
