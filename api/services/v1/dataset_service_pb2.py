# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/services/v1/dataset_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.services.v1 import dataset_service_models_pb2 as api_dot_services_dot_v1_dot_dataset__service__models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/services/v1/dataset_service.proto',
  package='api.services.v1',
  syntax='proto3',
  serialized_options=b'\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\017DatasetServicesP\001Z2github.com/ScienceObjectsDB/go-api/api/services/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%api/services/v1/dataset_service.proto\x12\x0f\x61pi.services.v1\x1a,api/services/v1/dataset_service_models.proto\x1a\x1cgoogle/api/annotations.proto2\x98\r\n\x0e\x44\x61tasetService\x12\x81\x01\n\rCreateDataset\x12%.api.services.v1.CreateDatasetRequest\x1a&.api.services.v1.CreateDatasetResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/api/v1/dataset/create:\x01*\x12u\n\nGetDataset\x12\".api.services.v1.GetDatasetRequest\x1a#.api.services.v1.GetDatasetResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\"\x13/api/v1/dataset/get:\x01*\x12\x96\x01\n\x12GetDatasetVersions\x12*.api.services.v1.GetDatasetVersionsRequest\x1a+.api.services.v1.GetDatasetVersionsResponse\"\'\x82\xd3\xe4\x93\x02!\"\x1c/api/v1/datasetversions/list:\x01*\x12\x9a\x01\n\x16GetDatasetObjectGroups\x12..api.services.v1.GetDatasetObjectGroupsRequest\x1a/.api.services.v1.GetDatasetObjectGroupsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/api/v1/dataset/list:\x01*\x12\xc4\x01\n\x1eGetCurrentObjectGroupRevisions\x12\x36.api.services.v1.GetCurrentObjectGroupRevisionsRequest\x1a\x37.api.services.v1.GetCurrentObjectGroupRevisionsResponse\"1\x82\xd3\xe4\x93\x02+\x12)/api/v1/dataset/{id}/currentgroupversions\x12\x90\x01\n\x12UpdateDatasetField\x12*.api.services.v1.UpdateDatasetFieldRequest\x1a+.api.services.v1.UpdateDatasetFieldResponse\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/api/v1/dataset/update:\x01*\x12|\n\rDeleteDataset\x12%.api.services.v1.DeleteDatasetRequest\x1a&.api.services.v1.DeleteDatasetResponse\"\x1c\x82\xd3\xe4\x93\x02\x16*\x14/api/v1/dataset/{id}\x12\xa0\x01\n\x15ReleaseDatasetVersion\x12-.api.services.v1.ReleaseDatasetVersionRequest\x1a..api.services.v1.ReleaseDatasetVersionResponse\"(\x82\xd3\xe4\x93\x02\"\"\x1d/api/v1/datasetversion/create:\x01*\x12\x91\x01\n\x11GetDatasetVersion\x12).api.services.v1.GetDatasetVersionRequest\x1a*.api.services.v1.GetDatasetVersionResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/api/v1/datasetversion/get:\x01*\x12\xaa\x01\n\x19GetDatsetVersionRevisions\x12\x31.api.services.v1.GetDatsetVersionRevisionsRequest\x1a\x32.api.services.v1.GetDatsetVersionRevisionsResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/api/v1/datasetversion/list:\x01*\x12\x98\x01\n\x14\x44\x65leteDatasetVersion\x12,.api.services.v1.DeleteDatasetVersionRequest\x1a-.api.services.v1.DeleteDatasetVersionResponse\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/api/v1/datasetversion/{id}B}\n4com.github.ScienceObjectsDB.java_api.api.services.v1B\x0f\x44\x61tasetServicesP\x01Z2github.com/ScienceObjectsDB/go-api/api/services/v1b\x06proto3'
  ,
  dependencies=[api_dot_services_dot_v1_dot_dataset__service__models__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_DATASETSERVICE = _descriptor.ServiceDescriptor(
  name='DatasetService',
  full_name='api.services.v1.DatasetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=135,
  serialized_end=1823,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateDataset',
    full_name='api.services.v1.DatasetService.CreateDataset',
    index=0,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._CREATEDATASETREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._CREATEDATASETRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\"\026/api/v1/dataset/create:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDataset',
    full_name='api.services.v1.DatasetService.GetDataset',
    index=1,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETRESPONSE,
    serialized_options=b'\202\323\344\223\002\030\"\023/api/v1/dataset/get:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatasetVersions',
    full_name='api.services.v1.DatasetService.GetDatasetVersions',
    index=2,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETVERSIONSREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETVERSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002!\"\034/api/v1/datasetversions/list:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatasetObjectGroups',
    full_name='api.services.v1.DatasetService.GetDatasetObjectGroups',
    index=3,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETOBJECTGROUPSREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETOBJECTGROUPSRESPONSE,
    serialized_options=b'\202\323\344\223\002\031\"\024/api/v1/dataset/list:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetCurrentObjectGroupRevisions',
    full_name='api.services.v1.DatasetService.GetCurrentObjectGroupRevisions',
    index=4,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETCURRENTOBJECTGROUPREVISIONSREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETCURRENTOBJECTGROUPREVISIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/api/v1/dataset/{id}/currentgroupversions',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDatasetField',
    full_name='api.services.v1.DatasetService.UpdateDatasetField',
    index=5,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._UPDATEDATASETFIELDREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._UPDATEDATASETFIELDRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\"\026/api/v1/dataset/update:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDataset',
    full_name='api.services.v1.DatasetService.DeleteDataset',
    index=6,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._DELETEDATASETREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._DELETEDATASETRESPONSE,
    serialized_options=b'\202\323\344\223\002\026*\024/api/v1/dataset/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReleaseDatasetVersion',
    full_name='api.services.v1.DatasetService.ReleaseDatasetVersion',
    index=7,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._RELEASEDATASETVERSIONREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._RELEASEDATASETVERSIONRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\"\035/api/v1/datasetversion/create:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatasetVersion',
    full_name='api.services.v1.DatasetService.GetDatasetVersion',
    index=8,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETVERSIONREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATASETVERSIONRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\"\032/api/v1/datasetversion/get:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDatsetVersionRevisions',
    full_name='api.services.v1.DatasetService.GetDatsetVersionRevisions',
    index=9,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATSETVERSIONREVISIONSREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._GETDATSETVERSIONREVISIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002 \"\033/api/v1/datasetversion/list:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteDatasetVersion',
    full_name='api.services.v1.DatasetService.DeleteDatasetVersion',
    index=10,
    containing_service=None,
    input_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._DELETEDATASETVERSIONREQUEST,
    output_type=api_dot_services_dot_v1_dot_dataset__service__models__pb2._DELETEDATASETVERSIONRESPONSE,
    serialized_options=b'\202\323\344\223\002\035*\033/api/v1/datasetversion/{id}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASETSERVICE)

DESCRIPTOR.services_by_name['DatasetService'] = _DATASETSERVICE

# @@protoc_insertion_point(module_scope)
