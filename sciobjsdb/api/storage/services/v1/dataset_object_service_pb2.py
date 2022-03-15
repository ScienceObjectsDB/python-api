# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/services/v1/dataset_object_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sciobjsdb.api.storage.services.v1 import dataset_object_service_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_services_dot_v1_dot_dataset__object__service__models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>sciobjsdb/api/storage/services/v1/dataset_object_service.proto\x12!sciobjsdb.api.storage.services.v1\x1a\x45sciobjsdb/api/storage/services/v1/dataset_object_service_models.proto\x1a\x1cgoogle/api/annotations.proto2\xfa\x08\n\x15\x44\x61tasetObjectsService\x12\xb5\x01\n\x11\x43reateObjectGroup\x12;.sciobjsdb.api.storage.services.v1.CreateObjectGroupRequest\x1a<.sciobjsdb.api.storage.services.v1.CreateObjectGroupResponse\"%\x82\xd3\xe4\x93\x02\x1f:\x01*\"\x1a/api/v1/objectgroup/create\x12\xc9\x01\n\x16\x43reateObjectGroupBatch\x12@.sciobjsdb.api.storage.services.v1.CreateObjectGroupBatchRequest\x1a\x41.sciobjsdb.api.storage.services.v1.CreateObjectGroupBatchResponse\"*\x82\xd3\xe4\x93\x02$:\x01*\"\x1f/api/v1/objectgroupbatch/create\x12\xa9\x01\n\x0eGetObjectGroup\x12\x38.sciobjsdb.api.storage.services.v1.GetObjectGroupRequest\x1a\x39.sciobjsdb.api.storage.services.v1.GetObjectGroupResponse\"\"\x82\xd3\xe4\x93\x02\x1c:\x01*\"\x17/api/v1/objectgroup/get\x12\xb3\x01\n\x12\x46inishObjectUpload\x12<.sciobjsdb.api.storage.services.v1.FinishObjectUploadRequest\x1a=.sciobjsdb.api.storage.services.v1.FinishObjectUploadResponse\" \x82\xd3\xe4\x93\x02\x1a:\x01*\"\x15/api/v1/object/finish\x12\xc7\x01\n\x17\x46inishObjectGroupUpload\x12\x41.sciobjsdb.api.storage.services.v1.FinishObjectGroupUploadRequest\x1a\x42.sciobjsdb.api.storage.services.v1.FinishObjectGroupUploadResponse\"%\x82\xd3\xe4\x93\x02\x1f:\x01*\"\x1a/api/v1/objectgroup/finish\x12\xb0\x01\n\x11\x44\x65leteObjectGroup\x12;.sciobjsdb.api.storage.services.v1.DeleteObjectGroupRequest\x1a<.sciobjsdb.api.storage.services.v1.DeleteObjectGroupResponse\" \x82\xd3\xe4\x93\x02\x1a*\x18/api/v1/objectgroup/{id}B\xa8\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x16\x44\x61tasetObjectsServicesP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')



_DATASETOBJECTSSERVICE = DESCRIPTOR.services_by_name['DatasetObjectsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\026DatasetObjectsServicesP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _DATASETOBJECTSSERVICE.methods_by_name['CreateObjectGroup']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['CreateObjectGroup']._serialized_options = b'\202\323\344\223\002\037:\001*\"\032/api/v1/objectgroup/create'
  _DATASETOBJECTSSERVICE.methods_by_name['CreateObjectGroupBatch']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['CreateObjectGroupBatch']._serialized_options = b'\202\323\344\223\002$:\001*\"\037/api/v1/objectgroupbatch/create'
  _DATASETOBJECTSSERVICE.methods_by_name['GetObjectGroup']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['GetObjectGroup']._serialized_options = b'\202\323\344\223\002\034:\001*\"\027/api/v1/objectgroup/get'
  _DATASETOBJECTSSERVICE.methods_by_name['FinishObjectUpload']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['FinishObjectUpload']._serialized_options = b'\202\323\344\223\002\032:\001*\"\025/api/v1/object/finish'
  _DATASETOBJECTSSERVICE.methods_by_name['FinishObjectGroupUpload']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['FinishObjectGroupUpload']._serialized_options = b'\202\323\344\223\002\037:\001*\"\032/api/v1/objectgroup/finish'
  _DATASETOBJECTSSERVICE.methods_by_name['DeleteObjectGroup']._options = None
  _DATASETOBJECTSSERVICE.methods_by_name['DeleteObjectGroup']._serialized_options = b'\202\323\344\223\002\032*\030/api/v1/objectgroup/{id}'
  _DATASETOBJECTSSERVICE._serialized_start=203
  _DATASETOBJECTSSERVICE._serialized_end=1349
# @@protoc_insertion_point(module_scope)
