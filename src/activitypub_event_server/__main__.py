import asyncio
import logging

from activitypub_event_server.service import execute

_log = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    _log.info("Starting service...")

    _log.info("Service started.")
    asyncio.run(execute())
