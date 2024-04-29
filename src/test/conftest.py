import json

import pytest


@pytest.fixture
def event_fixture():
    event_json = {
        "@context": "https://www.w3.org/ns/activitystreams",
        "type": "Event",
        "name": "A simple event",
        "startTime": "2020-01-01T00:00:00Z",
        "endTime": "2020-01-01T01:00:00Z",
    }

    return json.dumps(event_json)
