# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/models/v1/object_models.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3sciobjsdb/api/storage/models/v1/object_models.proto\x12\x1fsciobjsdb.api.storage.models.v1\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd5\x04\n\x0bObjectGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\ndataset_id\x18\x04 \x01(\tR\tdatasetId\x12\x1d\n\nproject_id\x18\x05 \x01(\tR\tprojectId\x12>\n\x06labels\x18\x06 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12\x45\n\x08metadata\x18\x07 \x03(\x0b\x32).sciobjsdb.api.storage.models.v1.MetadataR\x08metadata\x12?\n\x06status\x18\x08 \x01(\x0e\x32\'.sciobjsdb.api.storage.models.v1.StatusR\x06status\x12\x41\n\x07objects\x18\t \x03(\x0b\x32\'.sciobjsdb.api.storage.models.v1.ObjectR\x07objects\x12\x38\n\tgenerated\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tgenerated\x12\x34\n\x07\x63reated\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12G\n\x05stats\x18\x0c \x01(\x0b\x32\x31.sciobjsdb.api.storage.models.v1.ObjectGroupStatsR\x05stats\"x\n\x10ObjectGroupStats\x12!\n\x0cobject_count\x18\x01 \x01(\x03R\x0bobjectCount\x12\x19\n\x08\x61\x63\x63_size\x18\x02 \x01(\x03R\x07\x61\x63\x63Size\x12&\n\x0f\x61vg_object_size\x18\x03 \x01(\x01R\ravgObjectSize\"\xf8\x05\n\x06Object\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x1a\n\x08\x66iletype\x18\x03 \x01(\tR\x08\x66iletype\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12\x45\n\x08metadata\x18\x05 \x03(\x0b\x32).sciobjsdb.api.storage.models.v1.MetadataR\x08metadata\x12\x34\n\x07\x63reated\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x63reated\x12\x45\n\x08location\x18\x07 \x01(\x0b\x32).sciobjsdb.api.storage.models.v1.LocationR\x08location\x12?\n\x06origin\x18\x08 \x01(\x0b\x32\'.sciobjsdb.api.storage.models.v1.OriginR\x06origin\x12\x1f\n\x0b\x63ontent_len\x18\t \x01(\x03R\ncontentLen\x12\x1b\n\tupload_id\x18\n \x01(\tR\x08uploadId\x12\x38\n\tgenerated\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tgenerated\x12&\n\x0fobject_group_id\x18\x0c \x01(\tR\robjectGroupId\x12\x1d\n\ndataset_id\x18\r \x01(\tR\tdatasetId\x12\x1d\n\nproject_id\x18\x0e \x01(\tR\tprojectId\x12?\n\x06status\x18\x0f \x01(\x0e\x32\'.sciobjsdb.api.storage.models.v1.StatusR\x06status\x12\x42\n\x05stats\x18\x10 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.ObjectStatsR\x05stats\"\r\n\x0bObjectStatsB\x9a\x01\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\x0cObjectModelsP\x01ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sciobjsdb.api.storage.models.v1.object_models_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nDcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.models.v1B\014ObjectModelsP\001ZBgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/models/v1'
  _OBJECTGROUP._serialized_start=175
  _OBJECTGROUP._serialized_end=772
  _OBJECTGROUPSTATS._serialized_start=774
  _OBJECTGROUPSTATS._serialized_end=894
  _OBJECT._serialized_start=897
  _OBJECT._serialized_end=1657
  _OBJECTSTATS._serialized_start=1659
  _OBJECTSTATS._serialized_end=1672
# @@protoc_insertion_point(module_scope)
