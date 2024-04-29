"""Stub container for the generated gRPC client stubs."""

import grpc
from protos import event_core


# write a StubContainer for requests and response
class AppStubContainer(grpc.aio.StubContainer):
    event = event_core.EventServiceStub
