"""Tests for activitypub event parsing."""

from asyncio_play import event_parsing


# write a test that can parse a simple event into an object
def test_json_to_event_obj(event_fixture):
    """Test that the json_to_event_obj function can parse a simple event."""
    event = event_parsing.json_to_event_obj(event_fixture)
    assert event.name == "A simple event"
    assert event.start_time == "2020-01-01T00:00:00Z"
    assert event.end_time == "2020-01-01T01:00:00Z"
