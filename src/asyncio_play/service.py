"""Service for rest api adapter for grpc service."""

import asyncio
import logging
from grpc import server
from asyncio_play.protos import ServiceServicer, add_ServiceServicer_to_server

_log = logging.getLogger(__name__)

async def execute():
    """Execute the service."""
    _log.info("Executing service...")

    # Start a server
    server = server()

    # Add event service seriver to server
    add_ServiceServicer_to_server(ServiceServicer(), server)

    # Configure and start the server
    server.add_insecure_port("[::]:50051")
    server.start()

    try:    
        while True: 
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    _log.info("Starting service...")

    _log.info("Service started.")
    asyncio.run(execute())