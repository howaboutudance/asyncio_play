# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x65vents.proto\x12\x06\x65vents\x1a\x1fgoogle/protobuf/timestamp.proto\"#\n\x0fGetEventRequest\x12\x10\n\x08\x65vent_id\x18\x01 \x01(\x05\"0\n\x10GetEventResponse\x12\x1c\n\x05\x65vent\x18\x01 \x01(\x0b\x32\r.events.Event\"0\n\x1fGetEventsChronologicallyRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\"A\n GetEventsChronologicallyResponse\x12\x1d\n\x06\x65vents\x18\x01 \x03(\x0b\x32\r.events.Event\"\xa2\x01\n\x05\x45vent\x12\x0f\n\x07\x63ontext\x18\x01 \x01(\t\x12\x10\n\x08\x65vent_id\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12-\n\tstartTime\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07\x65ndTime\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp2\xc0\x01\n\x0c\x45ventService\x12?\n\x08GetEvent\x12\x17.events.GetEventRequest\x1a\x18.events.GetEventResponse\"\x00\x12o\n\x18GetEventsChronologically\x12\'.events.GetEventsChronologicallyRequest\x1a(.events.GetEventsChronologicallyResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GETEVENTREQUEST']._serialized_start=57
  _globals['_GETEVENTREQUEST']._serialized_end=92
  _globals['_GETEVENTRESPONSE']._serialized_start=94
  _globals['_GETEVENTRESPONSE']._serialized_end=142
  _globals['_GETEVENTSCHRONOLOGICALLYREQUEST']._serialized_start=144
  _globals['_GETEVENTSCHRONOLOGICALLYREQUEST']._serialized_end=192
  _globals['_GETEVENTSCHRONOLOGICALLYRESPONSE']._serialized_start=194
  _globals['_GETEVENTSCHRONOLOGICALLYRESPONSE']._serialized_end=259
  _globals['_EVENT']._serialized_start=262
  _globals['_EVENT']._serialized_end=424
  _globals['_EVENTSERVICE']._serialized_start=427
  _globals['_EVENTSERVICE']._serialized_end=619
# @@protoc_insertion_point(module_scope)
