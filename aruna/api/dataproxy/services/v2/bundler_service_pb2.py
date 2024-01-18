# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/dataproxy/services/v2/bundler_service.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5aruna/api/dataproxy/services/v2/bundler_service.proto\x12\x1f\x61runa.api.dataproxy.services.v2\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/api/visibility.proto\x1a\x1cgoogle/api/annotations.proto\"\x8f\x01\n\x13\x43reateBundleRequest\x12!\n\x0cresource_ids\x18\x01 \x03(\tR\x0bresourceIds\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x39\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"R\n\x14\x43reateBundleResponse\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\x12\x1d\n\nbundle_url\x18\x02 \x01(\tR\tbundleUrl\"2\n\x13\x44\x65leteBundleRequest\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\"\x16\n\x14\x44\x65leteBundleResponse2\xd7\x02\n\x0e\x42undlerService\x12\x93\x01\n\x0c\x43reateBundle\x12\x34.aruna.api.dataproxy.services.v2.CreateBundleRequest\x1a\x35.aruna.api.dataproxy.services.v2.CreateBundleResponse\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0b/v2/bundles:\x01*\x12\x9f\x01\n\x0c\x44\x65leteBundle\x12\x34.aruna.api.dataproxy.services.v2.DeleteBundleRequest\x1a\x35.aruna.api.dataproxy.services.v2.DeleteBundleResponse\"\"\x82\xd3\xe4\x93\x02\x1c*\x17/v2/bundles/{bundle_id}:\x01*\x1a\r\xfa\xd2\xe4\x93\x02\x07\x12\x05PROXYB\x94\x01\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\x0e\x42undlerServiceP\x01Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.dataproxy.services.v2.bundler_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n@com.github.ArunaStorage.java_api.aruna.api.dataproxy.services.v2B\016BundlerServiceP\001Z>github.com/ArunaStorage/go-api/aruna/api/dataproxy/services/v2'
  _globals['_BUNDLERSERVICE']._options = None
  _globals['_BUNDLERSERVICE']._serialized_options = b'\372\322\344\223\002\007\022\005PROXY'
  _globals['_BUNDLERSERVICE'].methods_by_name['CreateBundle']._options = None
  _globals['_BUNDLERSERVICE'].methods_by_name['CreateBundle']._serialized_options = b'\202\323\344\223\002\020\"\013/v2/bundles:\001*'
  _globals['_BUNDLERSERVICE'].methods_by_name['DeleteBundle']._options = None
  _globals['_BUNDLERSERVICE'].methods_by_name['DeleteBundle']._serialized_options = b'\202\323\344\223\002\034*\027/v2/bundles/{bundle_id}:\001*'
  _globals['_CREATEBUNDLEREQUEST']._serialized_start=183
  _globals['_CREATEBUNDLEREQUEST']._serialized_end=326
  _globals['_CREATEBUNDLERESPONSE']._serialized_start=328
  _globals['_CREATEBUNDLERESPONSE']._serialized_end=410
  _globals['_DELETEBUNDLEREQUEST']._serialized_start=412
  _globals['_DELETEBUNDLEREQUEST']._serialized_end=462
  _globals['_DELETEBUNDLERESPONSE']._serialized_start=464
  _globals['_DELETEBUNDLERESPONSE']._serialized_end=486
  _globals['_BUNDLERSERVICE']._serialized_start=489
  _globals['_BUNDLERSERVICE']._serialized_end=832
# @@protoc_insertion_point(module_scope)
