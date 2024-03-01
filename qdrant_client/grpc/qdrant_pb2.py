# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qdrant.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import collections_service_pb2 as collections__service__pb2
from . import points_service_pb2 as points__service__pb2
from . import snapshots_service_pb2 as snapshots__service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cqdrant.proto\x12\x06qdrant\x1a\x19\x63ollections_service.proto\x1a\x14points_service.proto\x1a\x17snapshots_service.proto\"\x14\n\x12HealthCheckRequest\"R\n\x10HealthCheckReply\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x13\n\x06\x63ommit\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_commit2O\n\x06Qdrant\x12\x45\n\x0bHealthCheck\x12\x1a.qdrant.HealthCheckRequest\x1a\x18.qdrant.HealthCheckReply\"\x00\x42\x15\xaa\x02\x12Qdrant.Client.Grpcb\x06proto3')



_HEALTHCHECKREQUEST = DESCRIPTOR.message_types_by_name['HealthCheckRequest']
_HEALTHCHECKREPLY = DESCRIPTOR.message_types_by_name['HealthCheckReply']
HealthCheckRequest = _reflection.GeneratedProtocolMessageType('HealthCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKREQUEST,
  '__module__' : 'qdrant_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.HealthCheckRequest)
  })
_sym_db.RegisterMessage(HealthCheckRequest)

HealthCheckReply = _reflection.GeneratedProtocolMessageType('HealthCheckReply', (_message.Message,), {
  'DESCRIPTOR' : _HEALTHCHECKREPLY,
  '__module__' : 'qdrant_pb2'
  # @@protoc_insertion_point(class_scope:qdrant.HealthCheckReply)
  })
_sym_db.RegisterMessage(HealthCheckReply)

_QDRANT = DESCRIPTOR.services_by_name['Qdrant']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\022Qdrant.Client.Grpc'
  _HEALTHCHECKREQUEST._serialized_start=98
  _HEALTHCHECKREQUEST._serialized_end=118
  _HEALTHCHECKREPLY._serialized_start=120
  _HEALTHCHECKREPLY._serialized_end=202
  _QDRANT._serialized_start=204
  _QDRANT._serialized_end=283
# @@protoc_insertion_point(module_scope)
