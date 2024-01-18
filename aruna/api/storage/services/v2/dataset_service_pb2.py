# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v2/dataset_service.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v2 import models_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v2_dot_models__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import visibility_pb2 as google_dot_api_dot_visibility__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/storage/services/v2/dataset_service.proto\x12\x1d\x61runa.api.storage.services.v2\x1a(aruna/api/storage/models/v2/models.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/api/visibility.proto\"\x9b\x04\n\x14\x43reateDatasetRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x44\n\nkey_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\tkeyValues\x12\x43\n\trelations\x18\x04 \x03(\x0b\x32%.aruna.api.storage.models.v2.RelationR\trelations\x12\x45\n\ndata_class\x18\x05 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\x12\x1f\n\nproject_id\x18\x06 \x01(\tH\x00R\tprojectId\x12%\n\rcollection_id\x18\x07 \x01(\tH\x00R\x0c\x63ollectionId\x12\x35\n\x14metadata_license_tag\x18\x08 \x01(\tH\x01R\x12metadataLicenseTag\x88\x01\x01\x12<\n\x18\x64\x65\x66\x61ult_data_license_tag\x18\t \x01(\tH\x02R\x15\x64\x65\x66\x61ultDataLicenseTag\x88\x01\x01\x42\x08\n\x06parentB\x17\n\x15_metadata_license_tagB\x1b\n\x19_default_data_license_tag\"W\n\x15\x43reateDatasetResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"2\n\x11GetDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\"T\n\x12GetDatasetResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"5\n\x12GetDatasetsRequest\x12\x1f\n\x0b\x64\x61taset_ids\x18\x01 \x03(\tR\ndatasetIds\"W\n\x13GetDatasetsResponse\x12@\n\x08\x64\x61tasets\x18\x01 \x03(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x08\x64\x61tasets\"5\n\x14\x44\x65leteDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\"\x17\n\x15\x44\x65leteDatasetResponse\"M\n\x18UpdateDatasetNameRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"[\n\x19UpdateDatasetNameResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"b\n\x1fUpdateDatasetDescriptionRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"b\n UpdateDatasetDescriptionResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"\xde\x01\n\x1dUpdateDatasetKeyValuesRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12K\n\x0e\x61\x64\x64_key_values\x18\x02 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0c\x61\x64\x64KeyValues\x12Q\n\x11remove_key_values\x18\x03 \x03(\x0b\x32%.aruna.api.storage.models.v2.KeyValueR\x0fremoveKeyValues\"`\n\x1eUpdateDatasetKeyValuesResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"\x85\x01\n\x1dUpdateDatasetDataClassRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\x45\n\ndata_class\x18\x02 \x01(\x0e\x32&.aruna.api.storage.models.v2.DataClassR\tdataClass\"`\n\x1eUpdateDatasetDataClassResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"7\n\x16SnapshotDatasetRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\"Y\n\x17SnapshotDatasetResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset\"\xa8\x01\n\x1cUpdateDatasetLicensesRequest\x12\x1d\n\ndataset_id\x18\x01 \x01(\tR\tdatasetId\x12\x30\n\x14metadata_license_tag\x18\x02 \x01(\tR\x12metadataLicenseTag\x12\x37\n\x18\x64\x65\x66\x61ult_data_license_tag\x18\x03 \x01(\tR\x15\x64\x65\x66\x61ultDataLicenseTag\"_\n\x1dUpdateDatasetLicensesResponse\x12>\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32$.aruna.api.storage.models.v2.DatasetR\x07\x64\x61taset2\x86\x0e\n\x0e\x44\x61tasetService\x12\x93\x01\n\rCreateDataset\x12\x33.aruna.api.storage.services.v2.CreateDatasetRequest\x1a\x34.aruna.api.storage.services.v2.CreateDatasetResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v2/datasets:\x01*\x12\x94\x01\n\nGetDataset\x12\x30.aruna.api.storage.services.v2.GetDatasetRequest\x1a\x31.aruna.api.storage.services.v2.GetDatasetResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v2/datasets/{dataset_id}\x12\x8a\x01\n\x0bGetDatasets\x12\x31.aruna.api.storage.services.v2.GetDatasetsRequest\x1a\x32.aruna.api.storage.services.v2.GetDatasetsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v2/datasets\x12\x9d\x01\n\rDeleteDataset\x12\x33.aruna.api.storage.services.v2.DeleteDatasetRequest\x1a\x34.aruna.api.storage.services.v2.DeleteDatasetResponse\"!\x82\xd3\xe4\x93\x02\x1b*\x19/v2/datasets/{dataset_id}\x12\xb1\x01\n\x11UpdateDatasetName\x12\x37.aruna.api.storage.services.v2.UpdateDatasetNameRequest\x1a\x38.aruna.api.storage.services.v2.UpdateDatasetNameResponse\")\x82\xd3\xe4\x93\x02#2\x1e/v2/datasets/{dataset_id}/name:\x01*\x12\xcd\x01\n\x18UpdateDatasetDescription\x12>.aruna.api.storage.services.v2.UpdateDatasetDescriptionRequest\x1a?.aruna.api.storage.services.v2.UpdateDatasetDescriptionResponse\"0\x82\xd3\xe4\x93\x02*2%/v2/datasets/{dataset_id}/description:\x01*\x12\xc6\x01\n\x16UpdateDatasetKeyValues\x12<.aruna.api.storage.services.v2.UpdateDatasetKeyValuesRequest\x1a=.aruna.api.storage.services.v2.UpdateDatasetKeyValuesResponse\"/\x82\xd3\xe4\x93\x02)2$/v2/datasets/{dataset_id}/key_values:\x01*\x12\xc6\x01\n\x16UpdateDatasetDataClass\x12<.aruna.api.storage.services.v2.UpdateDatasetDataClassRequest\x1a=.aruna.api.storage.services.v2.UpdateDatasetDataClassResponse\"/\x82\xd3\xe4\x93\x02)2$/v2/datasets/{dataset_id}/data_class:\x01*\x12\xaf\x01\n\x0fSnapshotDataset\x12\x35.aruna.api.storage.services.v2.SnapshotDatasetRequest\x1a\x36.aruna.api.storage.services.v2.SnapshotDatasetResponse\"-\x82\xd3\xe4\x93\x02\'\"\"/v2/datasets/{dataset_id}/snapshot:\x01*\x12\xc1\x01\n\x15UpdateDatasetLicenses\x12;.aruna.api.storage.services.v2.UpdateDatasetLicensesRequest\x1a<.aruna.api.storage.services.v2.UpdateDatasetLicensesResponse\"-\x82\xd3\xe4\x93\x02\'2\"/v2/datasets/{dataset_id}/licenses:\x01*\x1a\x0e\xfa\xd2\xe4\x93\x02\x08\x12\x06SERVERB\x93\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\x0e\x44\x61tasetServiceP\x01Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v2.dataset_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v2B\016DatasetServiceP\001Z?github.com/ArunaStorage/go-api/v2/aruna/api/storage/services/v2'
  _globals['_DATASETSERVICE']._options = None
  _globals['_DATASETSERVICE']._serialized_options = b'\372\322\344\223\002\010\022\006SERVER'
  _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['CreateDataset']._serialized_options = b'\202\323\344\223\002\021\"\014/v2/datasets:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._serialized_options = b'\202\323\344\223\002\033\022\031/v2/datasets/{dataset_id}'
  _globals['_DATASETSERVICE'].methods_by_name['GetDatasets']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['GetDatasets']._serialized_options = b'\202\323\344\223\002\016\022\014/v2/datasets'
  _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._serialized_options = b'\202\323\344\223\002\033*\031/v2/datasets/{dataset_id}'
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetName']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetName']._serialized_options = b'\202\323\344\223\002#2\036/v2/datasets/{dataset_id}/name:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetDescription']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetDescription']._serialized_options = b'\202\323\344\223\002*2%/v2/datasets/{dataset_id}/description:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetKeyValues']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetKeyValues']._serialized_options = b'\202\323\344\223\002)2$/v2/datasets/{dataset_id}/key_values:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetDataClass']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetDataClass']._serialized_options = b'\202\323\344\223\002)2$/v2/datasets/{dataset_id}/data_class:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['SnapshotDataset']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['SnapshotDataset']._serialized_options = b'\202\323\344\223\002\'\"\"/v2/datasets/{dataset_id}/snapshot:\001*'
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetLicenses']._options = None
  _globals['_DATASETSERVICE'].methods_by_name['UpdateDatasetLicenses']._serialized_options = b'\202\323\344\223\002\'2\"/v2/datasets/{dataset_id}/licenses:\001*'
  _globals['_CREATEDATASETREQUEST']._serialized_start=188
  _globals['_CREATEDATASETREQUEST']._serialized_end=727
  _globals['_CREATEDATASETRESPONSE']._serialized_start=729
  _globals['_CREATEDATASETRESPONSE']._serialized_end=816
  _globals['_GETDATASETREQUEST']._serialized_start=818
  _globals['_GETDATASETREQUEST']._serialized_end=868
  _globals['_GETDATASETRESPONSE']._serialized_start=870
  _globals['_GETDATASETRESPONSE']._serialized_end=954
  _globals['_GETDATASETSREQUEST']._serialized_start=956
  _globals['_GETDATASETSREQUEST']._serialized_end=1009
  _globals['_GETDATASETSRESPONSE']._serialized_start=1011
  _globals['_GETDATASETSRESPONSE']._serialized_end=1098
  _globals['_DELETEDATASETREQUEST']._serialized_start=1100
  _globals['_DELETEDATASETREQUEST']._serialized_end=1153
  _globals['_DELETEDATASETRESPONSE']._serialized_start=1155
  _globals['_DELETEDATASETRESPONSE']._serialized_end=1178
  _globals['_UPDATEDATASETNAMEREQUEST']._serialized_start=1180
  _globals['_UPDATEDATASETNAMEREQUEST']._serialized_end=1257
  _globals['_UPDATEDATASETNAMERESPONSE']._serialized_start=1259
  _globals['_UPDATEDATASETNAMERESPONSE']._serialized_end=1350
  _globals['_UPDATEDATASETDESCRIPTIONREQUEST']._serialized_start=1352
  _globals['_UPDATEDATASETDESCRIPTIONREQUEST']._serialized_end=1450
  _globals['_UPDATEDATASETDESCRIPTIONRESPONSE']._serialized_start=1452
  _globals['_UPDATEDATASETDESCRIPTIONRESPONSE']._serialized_end=1550
  _globals['_UPDATEDATASETKEYVALUESREQUEST']._serialized_start=1553
  _globals['_UPDATEDATASETKEYVALUESREQUEST']._serialized_end=1775
  _globals['_UPDATEDATASETKEYVALUESRESPONSE']._serialized_start=1777
  _globals['_UPDATEDATASETKEYVALUESRESPONSE']._serialized_end=1873
  _globals['_UPDATEDATASETDATACLASSREQUEST']._serialized_start=1876
  _globals['_UPDATEDATASETDATACLASSREQUEST']._serialized_end=2009
  _globals['_UPDATEDATASETDATACLASSRESPONSE']._serialized_start=2011
  _globals['_UPDATEDATASETDATACLASSRESPONSE']._serialized_end=2107
  _globals['_SNAPSHOTDATASETREQUEST']._serialized_start=2109
  _globals['_SNAPSHOTDATASETREQUEST']._serialized_end=2164
  _globals['_SNAPSHOTDATASETRESPONSE']._serialized_start=2166
  _globals['_SNAPSHOTDATASETRESPONSE']._serialized_end=2255
  _globals['_UPDATEDATASETLICENSESREQUEST']._serialized_start=2258
  _globals['_UPDATEDATASETLICENSESREQUEST']._serialized_end=2426
  _globals['_UPDATEDATASETLICENSESRESPONSE']._serialized_start=2428
  _globals['_UPDATEDATASETLICENSESRESPONSE']._serialized_end=2523
  _globals['_DATASETSERVICE']._serialized_start=2526
  _globals['_DATASETSERVICE']._serialized_end=4324
# @@protoc_insertion_point(module_scope)
