# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/health/v2/health.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n aruna/api/health/v2/health.proto\x12\x13\x61runa.api.health.v2\x1a\x1bgoogle/api/visibility.proto\".\n\x12HealthCheckRequest\x12\x18\n\x07service\x18\x01 \x01(\tR\x07service\"\xb6\x01\n\x13HealthCheckResponse\x12N\n\x06status\x18\x01 \x01(\x0e\x32\x36.aruna.api.health.v2.HealthCheckResponse.ServingStatusR\x06status\"O\n\rServingStatus\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SERVING\x10\x01\x12\x0f\n\x0bNOT_SERVING\x10\x02\x12\x13\n\x0fSERVICE_UNKNOWN\x10\x03\x32\xd4\x01\n\x06Health\x12Z\n\x05\x43heck\x12\'.aruna.api.health.v2.HealthCheckRequest\x1a(.aruna.api.health.v2.HealthCheckResponse\x12\\\n\x05Watch\x12\'.aruna.api.health.v2.HealthCheckRequest\x1a(.aruna.api.health.v2.HealthCheckResponse0\x01\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB}\n4com.github.ArunaStorage.java_api.aruna.api.health.v2B\x0cHooksServiceP\x01Z5github.com/ArunaStorage/go-api/v2/aruna/api/health/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.health.v2.health_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n4com.github.ArunaStorage.java_api.aruna.api.health.v2B\014HooksServiceP\001Z5github.com/ArunaStorage/go-api/v2/aruna/api/health/v2'
  _globals['_HEALTH']._options = None
  _globals['_HEALTH']._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _globals['_HEALTHCHECKREQUEST']._serialized_start=86
  _globals['_HEALTHCHECKREQUEST']._serialized_end=132
  _globals['_HEALTHCHECKRESPONSE']._serialized_start=135
  _globals['_HEALTHCHECKRESPONSE']._serialized_end=317
  _globals['_HEALTHCHECKRESPONSE_SERVINGSTATUS']._serialized_start=238
  _globals['_HEALTHCHECKRESPONSE_SERVINGSTATUS']._serialized_end=317
  _globals['_HEALTH']._serialized_start=320
  _globals['_HEALTH']._serialized_end=532
# @@protoc_insertion_point(module_scope)
