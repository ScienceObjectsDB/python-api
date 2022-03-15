# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sciobjsdb/api/storage/services/v1/dataset_service_models.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sciobjsdb.api.storage.models.v1 import dataset_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_dataset__pb2
from sciobjsdb.api.storage.models.v1 import common_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_common__models__pb2
from sciobjsdb.api.storage.models.v1 import object_models_pb2 as sciobjsdb_dot_api_dot_storage_dot_models_dot_v1_dot_object__models__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>sciobjsdb/api/storage/services/v1/dataset_service_models.proto\x12!sciobjsdb.api.storage.services.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a-sciobjsdb/api/storage/models/v1/dataset.proto\x1a\x33sciobjsdb/api/storage/models/v1/common_models.proto\x1a\x33sciobjsdb/api/storage/models/v1/object_models.proto\"\xf2\x01\n\x14\x43reateDatasetRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\x12>\n\x06labels\x18\x04 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12\x45\n\x08metadata\x18\x05 \x03(\x0b\x32).sciobjsdb.api.storage.models.v1.MetadataR\x08metadata\"\'\n\x15\x43reateDatasetResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"#\n\x11GetDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"X\n\x12GetDatasetResponse\x12\x42\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.DatasetR\x07\x64\x61taset\"+\n\x19GetDatasetVersionsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"x\n\x1aGetDatasetVersionsResponse\x12Z\n\x10\x64\x61taset_versions\x18\x01 \x03(\x0b\x32/.sciobjsdb.api.storage.models.v1.DatasetVersionR\x0f\x64\x61tasetVersions\"\x80\x01\n\x1dGetDatasetObjectGroupsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12O\n\x0cpage_request\x18\x02 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.PageRequestR\x0bpageRequest\"s\n\x1eGetDatasetObjectGroupsResponse\x12Q\n\robject_groups\x18\x01 \x03(\x0b\x32,.sciobjsdb.api.storage.models.v1.ObjectGroupR\x0cobjectGroups\"\x93\x01\n!GetObjectGroupsInDateRangeRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x30\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\"w\n\"GetObjectGroupsInDateRangeResponse\x12Q\n\robject_groups\x18\x01 \x03(\x0b\x32,.sciobjsdb.api.storage.models.v1.ObjectGroupR\x0cobjectGroups\"\x9a\t\n GetObjectGroupsStreamLinkRequest\x12o\n\x0bstream_type\x18\x03 \x01(\x0e\x32N.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.StreamTypeR\nstreamType\x12p\n\tgroup_ids\x18\x04 \x01(\x0b\x32Q.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.GroupIDsQueryH\x00R\x08groupIds\x12s\n\ndate_range\x18\x05 \x01(\x0b\x32R.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DateRangeQueryH\x00R\tdateRange\x12l\n\x07\x64\x61taset\x18\x06 \x01(\x0b\x32P.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetQueryH\x00R\x07\x64\x61taset\x12\x82\x01\n\x0f\x64\x61taset_version\x18\x07 \x01(\x0b\x32W.sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetVersionQueryH\x00R\x0e\x64\x61tasetVersion\x12\x32\n\x06\x65xpiry\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x06\x65xpiry\x1a\x8f\x01\n\x0e\x44\x61teRangeQuery\x12\x1d\n\ndataset_id\x18\x03 \x01(\tR\tdatasetId\x12\x30\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\x1aS\n\rGroupIDsQuery\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12#\n\robject_groups\x18\x01 \x03(\tR\x0cobjectGroups\x1a-\n\x0c\x44\x61tasetQuery\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x1a\x62\n\x13\x44\x61tasetVersionQuery\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12,\n\x12\x64\x61taset_version_id\x18\x02 \x01(\tR\x10\x64\x61tasetVersionId\"t\n\nStreamType\x12\x1b\n\x17STREAM_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19STREAM_TYPE_BASE64NEWLINE\x10\x01\x12\x13\n\x0fSTREAM_TYPE_ZIP\x10\x02\x12\x15\n\x11STREAM_TYPE_TARGZ\x10\x03\x42\x07\n\x05query\"5\n!GetObjectGroupsStreamLinkResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"x\n\x19UpdateDatasetFieldRequest\x12[\n\x0eupdate_request\x18\x01 \x01(\x0b\x32\x34.sciobjsdb.api.storage.models.v1.UpdateFieldsRequestR\rupdateRequest\"\x1c\n\x1aUpdateDatasetFieldResponse\"&\n\x14\x44\x65leteDatasetRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x17\n\x15\x44\x65leteDatasetResponse\"\xe8\x02\n\x1cReleaseDatasetVersionRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x1d\n\ndataset_id\x18\x02 \x01(\tR\tdatasetId\x12\x42\n\x07version\x18\x03 \x01(\x0b\x32(.sciobjsdb.api.storage.models.v1.VersionR\x07version\x12>\n\x06labels\x18\x05 \x03(\x0b\x32&.sciobjsdb.api.storage.models.v1.LabelR\x06labels\x12\x45\n\x08metadata\x18\x06 \x03(\x0b\x32).sciobjsdb.api.storage.models.v1.MetadataR\x08metadata\x12(\n\x10object_group_ids\x18\x07 \x03(\tR\x0eobjectGroupIds\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription\"/\n\x1dReleaseDatasetVersionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"*\n\x18GetDatasetVersionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"u\n\x19GetDatasetVersionResponse\x12X\n\x0f\x64\x61taset_version\x18\x01 \x01(\x0b\x32/.sciobjsdb.api.storage.models.v1.DatasetVersionR\x0e\x64\x61tasetVersion\"\x87\x01\n$GetDatasetVersionObjectGroupsRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12O\n\x0cpage_request\x18\x02 \x01(\x0b\x32,.sciobjsdb.api.storage.models.v1.PageRequestR\x0bpageRequest\"x\n%GetDatasetVersionObjectGroupsResponse\x12O\n\x0cobject_group\x18\x01 \x03(\x0b\x32,.sciobjsdb.api.storage.models.v1.ObjectGroupR\x0bobjectGroup\"-\n\x1b\x44\x65leteDatasetVersionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x1e\n\x1c\x44\x65leteDatasetVersionResponseB\xa6\x01\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\x14\x44\x61tasetServiceModelsP\x01ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1b\x06proto3')



_CREATEDATASETREQUEST = DESCRIPTOR.message_types_by_name['CreateDatasetRequest']
_CREATEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['CreateDatasetResponse']
_GETDATASETREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetRequest']
_GETDATASETRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetResponse']
_GETDATASETVERSIONSREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetVersionsRequest']
_GETDATASETVERSIONSRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetVersionsResponse']
_GETDATASETOBJECTGROUPSREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetObjectGroupsRequest']
_GETDATASETOBJECTGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetObjectGroupsResponse']
_GETOBJECTGROUPSINDATERANGEREQUEST = DESCRIPTOR.message_types_by_name['GetObjectGroupsInDateRangeRequest']
_GETOBJECTGROUPSINDATERANGERESPONSE = DESCRIPTOR.message_types_by_name['GetObjectGroupsInDateRangeResponse']
_GETOBJECTGROUPSSTREAMLINKREQUEST = DESCRIPTOR.message_types_by_name['GetObjectGroupsStreamLinkRequest']
_GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY = _GETOBJECTGROUPSSTREAMLINKREQUEST.nested_types_by_name['DateRangeQuery']
_GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY = _GETOBJECTGROUPSSTREAMLINKREQUEST.nested_types_by_name['GroupIDsQuery']
_GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY = _GETOBJECTGROUPSSTREAMLINKREQUEST.nested_types_by_name['DatasetQuery']
_GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY = _GETOBJECTGROUPSSTREAMLINKREQUEST.nested_types_by_name['DatasetVersionQuery']
_GETOBJECTGROUPSSTREAMLINKRESPONSE = DESCRIPTOR.message_types_by_name['GetObjectGroupsStreamLinkResponse']
_UPDATEDATASETFIELDREQUEST = DESCRIPTOR.message_types_by_name['UpdateDatasetFieldRequest']
_UPDATEDATASETFIELDRESPONSE = DESCRIPTOR.message_types_by_name['UpdateDatasetFieldResponse']
_DELETEDATASETREQUEST = DESCRIPTOR.message_types_by_name['DeleteDatasetRequest']
_DELETEDATASETRESPONSE = DESCRIPTOR.message_types_by_name['DeleteDatasetResponse']
_RELEASEDATASETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['ReleaseDatasetVersionRequest']
_RELEASEDATASETVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['ReleaseDatasetVersionResponse']
_GETDATASETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetVersionRequest']
_GETDATASETVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetVersionResponse']
_GETDATASETVERSIONOBJECTGROUPSREQUEST = DESCRIPTOR.message_types_by_name['GetDatasetVersionObjectGroupsRequest']
_GETDATASETVERSIONOBJECTGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['GetDatasetVersionObjectGroupsResponse']
_DELETEDATASETVERSIONREQUEST = DESCRIPTOR.message_types_by_name['DeleteDatasetVersionRequest']
_DELETEDATASETVERSIONRESPONSE = DESCRIPTOR.message_types_by_name['DeleteDatasetVersionResponse']
_GETOBJECTGROUPSSTREAMLINKREQUEST_STREAMTYPE = _GETOBJECTGROUPSSTREAMLINKREQUEST.enum_types_by_name['StreamType']
CreateDatasetRequest = _reflection.GeneratedProtocolMessageType('CreateDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.CreateDatasetRequest)
  })
_sym_db.RegisterMessage(CreateDatasetRequest)

CreateDatasetResponse = _reflection.GeneratedProtocolMessageType('CreateDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDATASETRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.CreateDatasetResponse)
  })
_sym_db.RegisterMessage(CreateDatasetResponse)

GetDatasetRequest = _reflection.GeneratedProtocolMessageType('GetDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetRequest)
  })
_sym_db.RegisterMessage(GetDatasetRequest)

GetDatasetResponse = _reflection.GeneratedProtocolMessageType('GetDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetResponse)
  })
_sym_db.RegisterMessage(GetDatasetResponse)

GetDatasetVersionsRequest = _reflection.GeneratedProtocolMessageType('GetDatasetVersionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONSREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionsRequest)
  })
_sym_db.RegisterMessage(GetDatasetVersionsRequest)

GetDatasetVersionsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetVersionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONSRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionsResponse)
  })
_sym_db.RegisterMessage(GetDatasetVersionsResponse)

GetDatasetObjectGroupsRequest = _reflection.GeneratedProtocolMessageType('GetDatasetObjectGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETOBJECTGROUPSREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetObjectGroupsRequest)
  })
_sym_db.RegisterMessage(GetDatasetObjectGroupsRequest)

GetDatasetObjectGroupsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetObjectGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETOBJECTGROUPSRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetObjectGroupsResponse)
  })
_sym_db.RegisterMessage(GetDatasetObjectGroupsResponse)

GetObjectGroupsInDateRangeRequest = _reflection.GeneratedProtocolMessageType('GetObjectGroupsInDateRangeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTGROUPSINDATERANGEREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsInDateRangeRequest)
  })
_sym_db.RegisterMessage(GetObjectGroupsInDateRangeRequest)

GetObjectGroupsInDateRangeResponse = _reflection.GeneratedProtocolMessageType('GetObjectGroupsInDateRangeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTGROUPSINDATERANGERESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsInDateRangeResponse)
  })
_sym_db.RegisterMessage(GetObjectGroupsInDateRangeResponse)

GetObjectGroupsStreamLinkRequest = _reflection.GeneratedProtocolMessageType('GetObjectGroupsStreamLinkRequest', (_message.Message,), {

  'DateRangeQuery' : _reflection.GeneratedProtocolMessageType('DateRangeQuery', (_message.Message,), {
    'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY,
    '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
    # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DateRangeQuery)
    })
  ,

  'GroupIDsQuery' : _reflection.GeneratedProtocolMessageType('GroupIDsQuery', (_message.Message,), {
    'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY,
    '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
    # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.GroupIDsQuery)
    })
  ,

  'DatasetQuery' : _reflection.GeneratedProtocolMessageType('DatasetQuery', (_message.Message,), {
    'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY,
    '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
    # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetQuery)
    })
  ,

  'DatasetVersionQuery' : _reflection.GeneratedProtocolMessageType('DatasetVersionQuery', (_message.Message,), {
    'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY,
    '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
    # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest.DatasetVersionQuery)
    })
  ,
  'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkRequest)
  })
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkRequest)
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkRequest.DateRangeQuery)
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkRequest.GroupIDsQuery)
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkRequest.DatasetQuery)
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkRequest.DatasetVersionQuery)

GetObjectGroupsStreamLinkResponse = _reflection.GeneratedProtocolMessageType('GetObjectGroupsStreamLinkResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETOBJECTGROUPSSTREAMLINKRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetObjectGroupsStreamLinkResponse)
  })
_sym_db.RegisterMessage(GetObjectGroupsStreamLinkResponse)

UpdateDatasetFieldRequest = _reflection.GeneratedProtocolMessageType('UpdateDatasetFieldRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETFIELDREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.UpdateDatasetFieldRequest)
  })
_sym_db.RegisterMessage(UpdateDatasetFieldRequest)

UpdateDatasetFieldResponse = _reflection.GeneratedProtocolMessageType('UpdateDatasetFieldResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDATASETFIELDRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.UpdateDatasetFieldResponse)
  })
_sym_db.RegisterMessage(UpdateDatasetFieldResponse)

DeleteDatasetRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.DeleteDatasetRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetRequest)

DeleteDatasetResponse = _reflection.GeneratedProtocolMessageType('DeleteDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.DeleteDatasetResponse)
  })
_sym_db.RegisterMessage(DeleteDatasetResponse)

ReleaseDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('ReleaseDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEDATASETVERSIONREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.ReleaseDatasetVersionRequest)
  })
_sym_db.RegisterMessage(ReleaseDatasetVersionRequest)

ReleaseDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('ReleaseDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _RELEASEDATASETVERSIONRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.ReleaseDatasetVersionResponse)
  })
_sym_db.RegisterMessage(ReleaseDatasetVersionResponse)

GetDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('GetDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionRequest)
  })
_sym_db.RegisterMessage(GetDatasetVersionRequest)

GetDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('GetDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionResponse)
  })
_sym_db.RegisterMessage(GetDatasetVersionResponse)

GetDatasetVersionObjectGroupsRequest = _reflection.GeneratedProtocolMessageType('GetDatasetVersionObjectGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONOBJECTGROUPSREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionObjectGroupsRequest)
  })
_sym_db.RegisterMessage(GetDatasetVersionObjectGroupsRequest)

GetDatasetVersionObjectGroupsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetVersionObjectGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETVERSIONOBJECTGROUPSRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.GetDatasetVersionObjectGroupsResponse)
  })
_sym_db.RegisterMessage(GetDatasetVersionObjectGroupsResponse)

DeleteDatasetVersionRequest = _reflection.GeneratedProtocolMessageType('DeleteDatasetVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETVERSIONREQUEST,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.DeleteDatasetVersionRequest)
  })
_sym_db.RegisterMessage(DeleteDatasetVersionRequest)

DeleteDatasetVersionResponse = _reflection.GeneratedProtocolMessageType('DeleteDatasetVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETVERSIONRESPONSE,
  '__module__' : 'sciobjsdb.api.storage.services.v1.dataset_service_models_pb2'
  # @@protoc_insertion_point(class_scope:sciobjsdb.api.storage.services.v1.DeleteDatasetVersionResponse)
  })
_sym_db.RegisterMessage(DeleteDatasetVersionResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nFcom.github.ScienceObjectsDB.java_api.sciobjsdb.api.storage.services.v1B\024DatasetServiceModelsP\001ZDgithub.com/ScienceObjectsDB/go-api/sciobjsdb/api/storage/services/v1'
  _CREATEDATASETREQUEST._serialized_start=288
  _CREATEDATASETREQUEST._serialized_end=530
  _CREATEDATASETRESPONSE._serialized_start=532
  _CREATEDATASETRESPONSE._serialized_end=571
  _GETDATASETREQUEST._serialized_start=573
  _GETDATASETREQUEST._serialized_end=608
  _GETDATASETRESPONSE._serialized_start=610
  _GETDATASETRESPONSE._serialized_end=698
  _GETDATASETVERSIONSREQUEST._serialized_start=700
  _GETDATASETVERSIONSREQUEST._serialized_end=743
  _GETDATASETVERSIONSRESPONSE._serialized_start=745
  _GETDATASETVERSIONSRESPONSE._serialized_end=865
  _GETDATASETOBJECTGROUPSREQUEST._serialized_start=868
  _GETDATASETOBJECTGROUPSREQUEST._serialized_end=996
  _GETDATASETOBJECTGROUPSRESPONSE._serialized_start=998
  _GETDATASETOBJECTGROUPSRESPONSE._serialized_end=1113
  _GETOBJECTGROUPSINDATERANGEREQUEST._serialized_start=1116
  _GETOBJECTGROUPSINDATERANGEREQUEST._serialized_end=1263
  _GETOBJECTGROUPSINDATERANGERESPONSE._serialized_start=1265
  _GETOBJECTGROUPSINDATERANGERESPONSE._serialized_end=1384
  _GETOBJECTGROUPSSTREAMLINKREQUEST._serialized_start=1387
  _GETOBJECTGROUPSSTREAMLINKREQUEST._serialized_end=2565
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY._serialized_start=2063
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATERANGEQUERY._serialized_end=2206
  _GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY._serialized_start=2208
  _GETOBJECTGROUPSSTREAMLINKREQUEST_GROUPIDSQUERY._serialized_end=2291
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY._serialized_start=2293
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETQUERY._serialized_end=2338
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY._serialized_start=2340
  _GETOBJECTGROUPSSTREAMLINKREQUEST_DATASETVERSIONQUERY._serialized_end=2438
  _GETOBJECTGROUPSSTREAMLINKREQUEST_STREAMTYPE._serialized_start=2440
  _GETOBJECTGROUPSSTREAMLINKREQUEST_STREAMTYPE._serialized_end=2556
  _GETOBJECTGROUPSSTREAMLINKRESPONSE._serialized_start=2567
  _GETOBJECTGROUPSSTREAMLINKRESPONSE._serialized_end=2620
  _UPDATEDATASETFIELDREQUEST._serialized_start=2622
  _UPDATEDATASETFIELDREQUEST._serialized_end=2742
  _UPDATEDATASETFIELDRESPONSE._serialized_start=2744
  _UPDATEDATASETFIELDRESPONSE._serialized_end=2772
  _DELETEDATASETREQUEST._serialized_start=2774
  _DELETEDATASETREQUEST._serialized_end=2812
  _DELETEDATASETRESPONSE._serialized_start=2814
  _DELETEDATASETRESPONSE._serialized_end=2837
  _RELEASEDATASETVERSIONREQUEST._serialized_start=2840
  _RELEASEDATASETVERSIONREQUEST._serialized_end=3200
  _RELEASEDATASETVERSIONRESPONSE._serialized_start=3202
  _RELEASEDATASETVERSIONRESPONSE._serialized_end=3249
  _GETDATASETVERSIONREQUEST._serialized_start=3251
  _GETDATASETVERSIONREQUEST._serialized_end=3293
  _GETDATASETVERSIONRESPONSE._serialized_start=3295
  _GETDATASETVERSIONRESPONSE._serialized_end=3412
  _GETDATASETVERSIONOBJECTGROUPSREQUEST._serialized_start=3415
  _GETDATASETVERSIONOBJECTGROUPSREQUEST._serialized_end=3550
  _GETDATASETVERSIONOBJECTGROUPSRESPONSE._serialized_start=3552
  _GETDATASETVERSIONOBJECTGROUPSRESPONSE._serialized_end=3672
  _DELETEDATASETVERSIONREQUEST._serialized_start=3674
  _DELETEDATASETVERSIONREQUEST._serialized_end=3719
  _DELETEDATASETVERSIONRESPONSE._serialized_start=3721
  _DELETEDATASETVERSIONRESPONSE._serialized_end=3751
# @@protoc_insertion_point(module_scope)
