"""Service for rest api adapter for grpc service."""

import asyncio
import logging
from concurrent import futures

from grpc import server as grpc_server

from activitypub_event_server.protos import add_EventServiceServicer_to_server
from activitypub_event_server.server import EventServiceService

_log = logging.getLogger(__name__)


async def execute():
    """Execute the service."""
    _log.info("Executing service...")

    # Start a server
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))

    # Add event service seriver to server
    add_EventServiceServicer_to_server(EventServiceService(), server)

    # Configure and start the server
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)
