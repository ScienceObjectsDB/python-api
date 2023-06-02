# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/internal/v1/bundler.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#aruna/api/internal/v1/bundler.proto\x12\x15\x61runa.api.internal.v1\x1a\x1bgoogle/api/visibility.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"3\n\x14PrepareBundleRequest\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\"\x17\n\x15PrepareBundleResponse\"|\n\tObjectRef\x12\'\n\x0fobject_location\x18\x01 \x01(\tR\x0eobjectLocation\x12%\n\x0e\x65ncryption_key\x18\x02 \x01(\tR\rencryptionKey\x12\x1f\n\x0bobject_path\x18\x03 \x01(\tR\nobjectPath\"\xa3\x01\n\x06\x42undle\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\x12\x41\n\x0bobject_refs\x18\x02 \x03(\x0b\x32 .aruna.api.internal.v1.ObjectRefR\nobjectRefs\x12\x39\n\nexpires_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\texpiresAt\"L\n\x13\x45nableBundleRequest\x12\x35\n\x06\x62undle\x18\x01 \x01(\x0b\x32\x1d.aruna.api.internal.v1.BundleR\x06\x62undle\"\x16\n\x14\x45nableBundleResponse\"\x13\n\x11GetBundlesRequest\"M\n\x12GetBundlesResponse\x12\x37\n\x07\x62undles\x18\x01 \x03(\x0b\x32\x1d.aruna.api.internal.v1.BundleR\x07\x62undles\"6\n\x17InvalidateBundleRequest\x12\x1b\n\tbundle_id\x18\x01 \x01(\tR\x08\x62undleId\"\x1a\n\x18InvalidateBundleResponse2\xfa\x02\n\x16InternalBundlerService\x12l\n\rPrepareBundle\x12+.aruna.api.internal.v1.PrepareBundleRequest\x1a,.aruna.api.internal.v1.PrepareBundleResponse\"\x00\x12i\n\x0c\x45nableBundle\x12*.aruna.api.internal.v1.EnableBundleRequest\x1a+.aruna.api.internal.v1.EnableBundleResponse\"\x00\x12u\n\x10InvalidateBundle\x12..aruna.api.internal.v1.InvalidateBundleRequest\x1a/.aruna.api.internal.v1.InvalidateBundleResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNAL2\x9a\x01\n!InternalBundlerBackchannelService\x12\x63\n\nGetBundles\x12(.aruna.api.internal.v1.GetBundlesRequest\x1a).aruna.api.internal.v1.GetBundlesResponse\"\x00\x1a\x10\xfa\xd2\xe4\x93\x02\n\x12\x08INTERNALB6Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.internal.v1.bundler_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z4github.com/ArunaStorage/go-api/aruna/api/internal/v1'
  _INTERNALBUNDLERSERVICE._options = None
  _INTERNALBUNDLERSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _INTERNALBUNDLERBACKCHANNELSERVICE._options = None
  _INTERNALBUNDLERBACKCHANNELSERVICE._serialized_options = b'\372\322\344\223\002\n\022\010INTERNAL'
  _PREPAREBUNDLEREQUEST._serialized_start=124
  _PREPAREBUNDLEREQUEST._serialized_end=175
  _PREPAREBUNDLERESPONSE._serialized_start=177
  _PREPAREBUNDLERESPONSE._serialized_end=200
  _OBJECTREF._serialized_start=202
  _OBJECTREF._serialized_end=326
  _BUNDLE._serialized_start=329
  _BUNDLE._serialized_end=492
  _ENABLEBUNDLEREQUEST._serialized_start=494
  _ENABLEBUNDLEREQUEST._serialized_end=570
  _ENABLEBUNDLERESPONSE._serialized_start=572
  _ENABLEBUNDLERESPONSE._serialized_end=594
  _GETBUNDLESREQUEST._serialized_start=596
  _GETBUNDLESREQUEST._serialized_end=615
  _GETBUNDLESRESPONSE._serialized_start=617
  _GETBUNDLESRESPONSE._serialized_end=694
  _INVALIDATEBUNDLEREQUEST._serialized_start=696
  _INVALIDATEBUNDLEREQUEST._serialized_end=750
  _INVALIDATEBUNDLERESPONSE._serialized_start=752
  _INVALIDATEBUNDLERESPONSE._serialized_end=778
  _INTERNALBUNDLERSERVICE._serialized_start=781
  _INTERNALBUNDLERSERVICE._serialized_end=1159
  _INTERNALBUNDLERBACKCHANNELSERVICE._serialized_start=1162
  _INTERNALBUNDLERBACKCHANNELSERVICE._serialized_end=1316
# @@protoc_insertion_point(module_scope)
