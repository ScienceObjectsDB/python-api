# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v1/project_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v1 import auth_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_auth__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3aruna/api/storage/services/v1/project_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a&aruna/api/storage/models/v1/auth.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"L\n\x14\x43reateProjectRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"6\n\x15\x43reateProjectResponse\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x91\x01\n\x17\x41\x64\x64UserToProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x03 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\x1a\n\x18\x41\x64\x64UserToProjectResponse\"2\n\x11GetProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\\\n\x12GetProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"\x14\n\x12GetProjectsRequest\"_\n\x13GetProjectsResponse\x12H\n\x08projects\x18\x01 \x03(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x08projects\"6\n\x15\x44\x65stroyProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"\x18\n\x16\x44\x65stroyProjectResponse\"k\n\x14UpdateProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"_\n\x15UpdateProjectResponse\x12\x46\n\x07project\x18\x01 \x01(\x0b\x32,.aruna.api.storage.models.v1.ProjectOverviewR\x07project\"V\n\x1cRemoveUserFromProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1f\n\x1dRemoveUserFromProjectResponse\"]\n#GetUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x8a\x01\n$GetUserPermissionsForProjectResponse\x12\x62\n\x0fuser_permission\x18\x01 \x01(\x0b\x32\x39.aruna.api.storage.models.v1.ProjectPermissionDisplayNameR\x0euserPermission\"\x9e\x01\n$EditUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12W\n\x0fuser_permission\x18\x02 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0euserPermission\"\'\n%EditUserPermissionsForProjectResponse\"\xae\x01\n\x1aUserWithProjectPermissions\x12\x35\n\x04user\x18\x01 \x01(\x0b\x32!.aruna.api.storage.models.v1.UserR\x04user\x12Y\n\x10user_permissions\x18\x02 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0fuserPermissions\"G\n&GetAllUserPermissionsForProjectRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\"z\n\'GetAllUserPermissionsForProjectResponse\x12O\n\x05users\x18\x01 \x03(\x0b\x32\x39.aruna.api.storage.services.v1.UserWithProjectPermissionsR\x05users2\x90\x0e\n\x0eProjectService\x12\x92\x01\n\rCreateProject\x12\x33.aruna.api.storage.services.v1.CreateProjectRequest\x1a\x34.aruna.api.storage.services.v1.CreateProjectResponse\"\x16\x82\xd3\xe4\x93\x02\x10:\x01*\"\x0b/v1/project\x12\xb1\x01\n\x10\x41\x64\x64UserToProject\x12\x36.aruna.api.storage.services.v1.AddUserToProjectRequest\x1a\x37.aruna.api.storage.services.v1.AddUserToProjectResponse\",\x82\xd3\xe4\x93\x02&:\x01*\"!/v1/project/{project_id}/add_user\x12\x93\x01\n\nGetProject\x12\x30.aruna.api.storage.services.v1.GetProjectRequest\x1a\x31.aruna.api.storage.services.v1.GetProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/project/{project_id}\x12\x8a\x01\n\x0bGetProjects\x12\x31.aruna.api.storage.services.v1.GetProjectsRequest\x1a\x32.aruna.api.storage.services.v1.GetProjectsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/projects\x12\x9f\x01\n\x0e\x44\x65stroyProject\x12\x34.aruna.api.storage.services.v1.DestroyProjectRequest\x1a\x35.aruna.api.storage.services.v1.DestroyProjectResponse\" \x82\xd3\xe4\x93\x02\x1a*\x18/v1/project/{project_id}\x12\x9c\x01\n\rUpdateProject\x12\x33.aruna.api.storage.services.v1.UpdateProjectRequest\x1a\x34.aruna.api.storage.services.v1.UpdateProjectResponse\" \x82\xd3\xe4\x93\x02\x1a\x1a\x18/v1/project/{project_id}\x12\xc0\x01\n\x15RemoveUserFromProject\x12;.aruna.api.storage.services.v1.RemoveUserFromProjectRequest\x1a<.aruna.api.storage.services.v1.RemoveUserFromProjectResponse\",\x82\xd3\xe4\x93\x02&*$/v1/project/{project_id}/remove_user\x12\xd2\x01\n\x1cGetUserPermissionsForProject\x12\x42.aruna.api.storage.services.v1.GetUserPermissionsForProjectRequest\x1a\x43.aruna.api.storage.services.v1.GetUserPermissionsForProjectResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/project/{project_id}/get_user\x12\xdc\x01\n\x1fGetAllUserPermissionsForProject\x12\x45.aruna.api.storage.services.v1.GetAllUserPermissionsForProjectRequest\x1a\x46.aruna.api.storage.services.v1.GetAllUserPermissionsForProjectResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/v1/project/{project_id}/get_users\x12\xd9\x01\n\x1d\x45\x64itUserPermissionsForProject\x12\x43.aruna.api.storage.services.v1.EditUserPermissionsForProjectRequest\x1a\x44.aruna.api.storage.services.v1.EditUserPermissionsForProjectResponse\"-\x82\xd3\xe4\x93\x02\':\x01*2\"/v1/project/{project_id}/edit_userB\xe5\x02\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0eProjectServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\x92\x41\xd1\x01\x12\x31\n#Aruna Object Storage (AOS) REST API2\n1.1.0-rc.2*\x01\x02\x32\x10\x61pplication/json:\x10\x61pplication/jsonZ`\n^\n\rAccessKeyAuth\x12M\x08\x02\x12\x38\x41uthentication token, prefixed by Bearer: Bearer <token>\x1a\rAuthorization \x02\x62\x13\n\x11\n\rAccessKeyAuth\x12\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v1.project_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\016ProjectServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1\222A\321\001\0221\n#Aruna Object Storage (AOS) REST API2\n1.1.0-rc.2*\001\0022\020application/json:\020application/jsonZ`\n^\n\rAccessKeyAuth\022M\010\002\0228Authentication token, prefixed by Bearer: Bearer <token>\032\rAuthorization \002b\023\n\021\n\rAccessKeyAuth\022\000'
  _PROJECTSERVICE.methods_by_name['CreateProject']._options = None
  _PROJECTSERVICE.methods_by_name['CreateProject']._serialized_options = b'\202\323\344\223\002\020:\001*\"\013/v1/project'
  _PROJECTSERVICE.methods_by_name['AddUserToProject']._options = None
  _PROJECTSERVICE.methods_by_name['AddUserToProject']._serialized_options = b'\202\323\344\223\002&:\001*\"!/v1/project/{project_id}/add_user'
  _PROJECTSERVICE.methods_by_name['GetProject']._options = None
  _PROJECTSERVICE.methods_by_name['GetProject']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/project/{project_id}'
  _PROJECTSERVICE.methods_by_name['GetProjects']._options = None
  _PROJECTSERVICE.methods_by_name['GetProjects']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/projects'
  _PROJECTSERVICE.methods_by_name['DestroyProject']._options = None
  _PROJECTSERVICE.methods_by_name['DestroyProject']._serialized_options = b'\202\323\344\223\002\032*\030/v1/project/{project_id}'
  _PROJECTSERVICE.methods_by_name['UpdateProject']._options = None
  _PROJECTSERVICE.methods_by_name['UpdateProject']._serialized_options = b'\202\323\344\223\002\032\032\030/v1/project/{project_id}'
  _PROJECTSERVICE.methods_by_name['RemoveUserFromProject']._options = None
  _PROJECTSERVICE.methods_by_name['RemoveUserFromProject']._serialized_options = b'\202\323\344\223\002&*$/v1/project/{project_id}/remove_user'
  _PROJECTSERVICE.methods_by_name['GetUserPermissionsForProject']._options = None
  _PROJECTSERVICE.methods_by_name['GetUserPermissionsForProject']._serialized_options = b'\202\323\344\223\002#\022!/v1/project/{project_id}/get_user'
  _PROJECTSERVICE.methods_by_name['GetAllUserPermissionsForProject']._options = None
  _PROJECTSERVICE.methods_by_name['GetAllUserPermissionsForProject']._serialized_options = b'\202\323\344\223\002$\022\"/v1/project/{project_id}/get_users'
  _PROJECTSERVICE.methods_by_name['EditUserPermissionsForProject']._options = None
  _PROJECTSERVICE.methods_by_name['EditUserPermissionsForProject']._serialized_options = b'\202\323\344\223\002\':\001*2\"/v1/project/{project_id}/edit_user'
  _CREATEPROJECTREQUEST._serialized_start=204
  _CREATEPROJECTREQUEST._serialized_end=280
  _CREATEPROJECTRESPONSE._serialized_start=282
  _CREATEPROJECTRESPONSE._serialized_end=336
  _ADDUSERTOPROJECTREQUEST._serialized_start=339
  _ADDUSERTOPROJECTREQUEST._serialized_end=484
  _ADDUSERTOPROJECTRESPONSE._serialized_start=486
  _ADDUSERTOPROJECTRESPONSE._serialized_end=512
  _GETPROJECTREQUEST._serialized_start=514
  _GETPROJECTREQUEST._serialized_end=564
  _GETPROJECTRESPONSE._serialized_start=566
  _GETPROJECTRESPONSE._serialized_end=658
  _GETPROJECTSREQUEST._serialized_start=660
  _GETPROJECTSREQUEST._serialized_end=680
  _GETPROJECTSRESPONSE._serialized_start=682
  _GETPROJECTSRESPONSE._serialized_end=777
  _DESTROYPROJECTREQUEST._serialized_start=779
  _DESTROYPROJECTREQUEST._serialized_end=833
  _DESTROYPROJECTRESPONSE._serialized_start=835
  _DESTROYPROJECTRESPONSE._serialized_end=859
  _UPDATEPROJECTREQUEST._serialized_start=861
  _UPDATEPROJECTREQUEST._serialized_end=968
  _UPDATEPROJECTRESPONSE._serialized_start=970
  _UPDATEPROJECTRESPONSE._serialized_end=1065
  _REMOVEUSERFROMPROJECTREQUEST._serialized_start=1067
  _REMOVEUSERFROMPROJECTREQUEST._serialized_end=1153
  _REMOVEUSERFROMPROJECTRESPONSE._serialized_start=1155
  _REMOVEUSERFROMPROJECTRESPONSE._serialized_end=1186
  _GETUSERPERMISSIONSFORPROJECTREQUEST._serialized_start=1188
  _GETUSERPERMISSIONSFORPROJECTREQUEST._serialized_end=1281
  _GETUSERPERMISSIONSFORPROJECTRESPONSE._serialized_start=1284
  _GETUSERPERMISSIONSFORPROJECTRESPONSE._serialized_end=1422
  _EDITUSERPERMISSIONSFORPROJECTREQUEST._serialized_start=1425
  _EDITUSERPERMISSIONSFORPROJECTREQUEST._serialized_end=1583
  _EDITUSERPERMISSIONSFORPROJECTRESPONSE._serialized_start=1585
  _EDITUSERPERMISSIONSFORPROJECTRESPONSE._serialized_end=1624
  _USERWITHPROJECTPERMISSIONS._serialized_start=1627
  _USERWITHPROJECTPERMISSIONS._serialized_end=1801
  _GETALLUSERPERMISSIONSFORPROJECTREQUEST._serialized_start=1803
  _GETALLUSERPERMISSIONSFORPROJECTREQUEST._serialized_end=1874
  _GETALLUSERPERMISSIONSFORPROJECTRESPONSE._serialized_start=1876
  _GETALLUSERPERMISSIONSFORPROJECTRESPONSE._serialized_end=1998
  _PROJECTSERVICE._serialized_start=2001
  _PROJECTSERVICE._serialized_end=3809
# @@protoc_insertion_point(module_scope)
