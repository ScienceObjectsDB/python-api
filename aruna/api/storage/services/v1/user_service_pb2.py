# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aruna/api/storage/services/v1/user_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aruna.api.storage.models.v1 import auth_pb2 as aruna_dot_api_dot_storage_dot_models_dot_v1_dot_auth__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0aruna/api/storage/services/v1/user_service.proto\x12\x1d\x61runa.api.storage.services.v1\x1a&aruna/api/storage/models/v1/auth.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"E\n\tExpiresAt\x12\x38\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimestamp\"h\n\x13RegisterUserRequest\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12\x14\n\x05\x65mail\x18\x02 \x01(\tR\x05\x65mail\x12\x18\n\x07project\x18\x03 \x01(\tR\x07project\"/\n\x14RegisterUserResponse\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\xa0\x02\n\x15\x43reateAPITokenRequest\x12\x1d\n\nproject_id\x18\x01 \x01(\tR\tprojectId\x12#\n\rcollection_id\x18\x02 \x01(\tR\x0c\x63ollectionId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12G\n\nexpires_at\x18\x04 \x01(\x0b\x32(.aruna.api.storage.services.v1.ExpiresAtR\texpiresAt\x12G\n\npermission\x18\x05 \x01(\x0e\x32\'.aruna.api.storage.models.v1.PermissionR\npermission\x12\x1d\n\nis_session\x18\x06 \x01(\x08R\tisSession\"\xbd\x01\n\x16\x43reateAPITokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v1.TokenR\x05token\x12!\n\x0ctoken_secret\x18\x02 \x01(\tR\x0btokenSecret\x12\"\n\rs3_access_key\x18\x03 \x01(\tR\x0bs3AccessKey\x12\"\n\rs3_secret_key\x18\x04 \x01(\tR\x0bs3SecretKey\"/\n\x12GetAPITokenRequest\x12\x19\n\x08token_id\x18\x01 \x01(\tR\x07tokenId\"O\n\x13GetAPITokenResponse\x12\x38\n\x05token\x18\x01 \x01(\x0b\x32\".aruna.api.storage.models.v1.TokenR\x05token\"\x15\n\x13GetAPITokensRequest\"P\n\x14GetAPITokensResponse\x12\x38\n\x05token\x18\x01 \x03(\x0b\x32\".aruna.api.storage.models.v1.TokenR\x05token\"2\n\x15\x44\x65leteAPITokenRequest\x12\x19\n\x08token_id\x18\x01 \x01(\tR\x07tokenId\"\x18\n\x16\x44\x65leteAPITokenResponse\"1\n\x16\x44\x65leteAPITokensRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x19\n\x17\x44\x65leteAPITokensResponse\")\n\x0eGetUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\xa9\x01\n\x0fGetUserResponse\x12\x35\n\x04user\x18\x01 \x01(\x0b\x32!.aruna.api.storage.models.v1.UserR\x04user\x12_\n\x13project_permissions\x18\x02 \x03(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x12projectPermissions\"H\n\x1cUpdateUserDisplayNameRequest\x12(\n\x10new_display_name\x18\x01 \x01(\tR\x0enewDisplayName\"V\n\x1dUpdateUserDisplayNameResponse\x12\x35\n\x04user\x18\x01 \x01(\x0b\x32!.aruna.api.storage.models.v1.UserR\x04user\"1\n\x16GetUserProjectsRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"S\n\x0bUserProject\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"a\n\x17GetUserProjectsResponse\x12\x46\n\x08projects\x18\x01 \x03(\x0b\x32*.aruna.api.storage.services.v1.UserProjectR\x08projects\"\x83\x01\n\x13\x41\x63tivateUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12S\n\rproject_perms\x18\x02 \x01(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0cprojectPerms\"\x16\n\x14\x41\x63tivateUserResponse\"\x1d\n\x1bGetNotActivatedUsersRequest\"W\n\x1cGetNotActivatedUsersResponse\x12\x37\n\x05users\x18\x01 \x03(\x0b\x32!.aruna.api.storage.models.v1.UserR\x05users\"E\n\x12GetAllUsersRequest\x12/\n\x13include_permissions\x18\x01 \x01(\x08R\x12includePermissions\"\x9b\x01\n\rUserWithPerms\x12\x35\n\x04user\x18\x01 \x01(\x0b\x32!.aruna.api.storage.models.v1.UserR\x04user\x12S\n\rproject_perms\x18\x02 \x03(\x0b\x32..aruna.api.storage.models.v1.ProjectPermissionR\x0cprojectPerms\"k\n\x13GetAllUsersResponse\x12T\n\x0fuser_with_perms\x18\x01 \x03(\x0b\x32,.aruna.api.storage.services.v1.UserWithPermsR\ruserWithPerms\"0\n\x15\x44\x65\x61\x63tivateUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"\x18\n\x16\x44\x65\x61\x63tivateUserResponse\"N\n\x16UpdateUserEmailRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tnew_email\x18\x02 \x01(\tR\x08newEmail\"P\n\x17UpdateUserEmailResponse\x12\x35\n\x04user\x18\x01 \x01(\x0b\x32!.aruna.api.storage.models.v1.UserR\x04user2\xb0\x11\n\x0bUserService\x12\x95\x01\n\x0cRegisterUser\x12\x32.aruna.api.storage.services.v1.RegisterUserRequest\x1a\x33.aruna.api.storage.services.v1.RegisterUserResponse\"\x1c\x82\xd3\xe4\x93\x02\x16:\x01*\"\x11/v1/auth/register\x12\xa7\x01\n\x0e\x44\x65\x61\x63tivateUser\x12\x34.aruna.api.storage.services.v1.DeactivateUserRequest\x1a\x35.aruna.api.storage.services.v1.DeactivateUserResponse\"(\x82\xd3\xe4\x93\x02\":\x01*2\x1d/v1/user/{user_id}/deactivate\x12\x9f\x01\n\x0c\x41\x63tivateUser\x12\x32.aruna.api.storage.services.v1.ActivateUserRequest\x1a\x33.aruna.api.storage.services.v1.ActivateUserResponse\"&\x82\xd3\xe4\x93\x02 :\x01*2\x1b/v1/user/{user_id}/activate\x12\x98\x01\n\x0e\x43reateAPIToken\x12\x34.aruna.api.storage.services.v1.CreateAPITokenRequest\x1a\x35.aruna.api.storage.services.v1.CreateAPITokenResponse\"\x19\x82\xd3\xe4\x93\x02\x13:\x01*\"\x0e/v1/auth/token\x12\x97\x01\n\x0bGetAPIToken\x12\x31.aruna.api.storage.services.v1.GetAPITokenRequest\x1a\x32.aruna.api.storage.services.v1.GetAPITokenResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/auth/token/{token_id}\x12\x90\x01\n\x0cGetAPITokens\x12\x32.aruna.api.storage.services.v1.GetAPITokensRequest\x1a\x33.aruna.api.storage.services.v1.GetAPITokensResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/auth/tokens\x12\xa0\x01\n\x0e\x44\x65leteAPIToken\x12\x34.aruna.api.storage.services.v1.DeleteAPITokenRequest\x1a\x35.aruna.api.storage.services.v1.DeleteAPITokenResponse\"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/auth/token/{token_id}\x12\x99\x01\n\x0f\x44\x65leteAPITokens\x12\x35.aruna.api.storage.services.v1.DeleteAPITokensRequest\x1a\x36.aruna.api.storage.services.v1.DeleteAPITokensResponse\"\x17\x82\xd3\xe4\x93\x02\x11*\x0f/v1/auth/tokens\x12z\n\x07GetUser\x12-.aruna.api.storage.services.v1.GetUserRequest\x1a..aruna.api.storage.services.v1.GetUserResponse\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/user\x12\xb4\x01\n\x15UpdateUserDisplayName\x12;.aruna.api.storage.services.v1.UpdateUserDisplayNameRequest\x1a<.aruna.api.storage.services.v1.UpdateUserDisplayNameResponse\" \x82\xd3\xe4\x93\x02\x1a:\x01*2\x15/v1/user/display_name\x12\x9b\x01\n\x0fUpdateUserEmail\x12\x35.aruna.api.storage.services.v1.UpdateUserEmailRequest\x1a\x36.aruna.api.storage.services.v1.UpdateUserEmailResponse\"\x19\x82\xd3\xe4\x93\x02\x13:\x01*2\x0e/v1/user/email\x12\xa5\x01\n\x0fGetUserProjects\x12\x35.aruna.api.storage.services.v1.GetUserProjectsRequest\x1a\x36.aruna.api.storage.services.v1.GetUserProjectsResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/user/{user_id}/projects\x12\xaf\x01\n\x14GetNotActivatedUsers\x12:.aruna.api.storage.services.v1.GetNotActivatedUsersRequest\x1a;.aruna.api.storage.services.v1.GetNotActivatedUsersResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/user/not_activated\x12\x8a\x01\n\x0bGetAllUsers\x12\x31.aruna.api.storage.services.v1.GetAllUsersRequest\x1a\x32.aruna.api.storage.services.v1.GetAllUsersResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/user/allB\x8d\x01\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\x0bUserServiceP\x01Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aruna.api.storage.services.v1.user_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n>com.github.ArunaStorage.java_api.aruna.api.storage.services.v1B\013UserServiceP\001Z<github.com/ArunaStorage/go-api/aruna/api/storage/services/v1'
  _USERSERVICE.methods_by_name['RegisterUser']._options = None
  _USERSERVICE.methods_by_name['RegisterUser']._serialized_options = b'\202\323\344\223\002\026:\001*\"\021/v1/auth/register'
  _USERSERVICE.methods_by_name['DeactivateUser']._options = None
  _USERSERVICE.methods_by_name['DeactivateUser']._serialized_options = b'\202\323\344\223\002\":\001*2\035/v1/user/{user_id}/deactivate'
  _USERSERVICE.methods_by_name['ActivateUser']._options = None
  _USERSERVICE.methods_by_name['ActivateUser']._serialized_options = b'\202\323\344\223\002 :\001*2\033/v1/user/{user_id}/activate'
  _USERSERVICE.methods_by_name['CreateAPIToken']._options = None
  _USERSERVICE.methods_by_name['CreateAPIToken']._serialized_options = b'\202\323\344\223\002\023:\001*\"\016/v1/auth/token'
  _USERSERVICE.methods_by_name['GetAPIToken']._options = None
  _USERSERVICE.methods_by_name['GetAPIToken']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/auth/token/{token_id}'
  _USERSERVICE.methods_by_name['GetAPITokens']._options = None
  _USERSERVICE.methods_by_name['GetAPITokens']._serialized_options = b'\202\323\344\223\002\021\022\017/v1/auth/tokens'
  _USERSERVICE.methods_by_name['DeleteAPIToken']._options = None
  _USERSERVICE.methods_by_name['DeleteAPIToken']._serialized_options = b'\202\323\344\223\002\033*\031/v1/auth/token/{token_id}'
  _USERSERVICE.methods_by_name['DeleteAPITokens']._options = None
  _USERSERVICE.methods_by_name['DeleteAPITokens']._serialized_options = b'\202\323\344\223\002\021*\017/v1/auth/tokens'
  _USERSERVICE.methods_by_name['GetUser']._options = None
  _USERSERVICE.methods_by_name['GetUser']._serialized_options = b'\202\323\344\223\002\n\022\010/v1/user'
  _USERSERVICE.methods_by_name['UpdateUserDisplayName']._options = None
  _USERSERVICE.methods_by_name['UpdateUserDisplayName']._serialized_options = b'\202\323\344\223\002\032:\001*2\025/v1/user/display_name'
  _USERSERVICE.methods_by_name['UpdateUserEmail']._options = None
  _USERSERVICE.methods_by_name['UpdateUserEmail']._serialized_options = b'\202\323\344\223\002\023:\001*2\016/v1/user/email'
  _USERSERVICE.methods_by_name['GetUserProjects']._options = None
  _USERSERVICE.methods_by_name['GetUserProjects']._serialized_options = b'\202\323\344\223\002\035\022\033/v1/user/{user_id}/projects'
  _USERSERVICE.methods_by_name['GetNotActivatedUsers']._options = None
  _USERSERVICE.methods_by_name['GetNotActivatedUsers']._serialized_options = b'\202\323\344\223\002\030\022\026/v1/user/not_activated'
  _USERSERVICE.methods_by_name['GetAllUsers']._options = None
  _USERSERVICE.methods_by_name['GetAllUsers']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/user/all'
  _EXPIRESAT._serialized_start=186
  _EXPIRESAT._serialized_end=255
  _REGISTERUSERREQUEST._serialized_start=257
  _REGISTERUSERREQUEST._serialized_end=361
  _REGISTERUSERRESPONSE._serialized_start=363
  _REGISTERUSERRESPONSE._serialized_end=410
  _CREATEAPITOKENREQUEST._serialized_start=413
  _CREATEAPITOKENREQUEST._serialized_end=701
  _CREATEAPITOKENRESPONSE._serialized_start=704
  _CREATEAPITOKENRESPONSE._serialized_end=893
  _GETAPITOKENREQUEST._serialized_start=895
  _GETAPITOKENREQUEST._serialized_end=942
  _GETAPITOKENRESPONSE._serialized_start=944
  _GETAPITOKENRESPONSE._serialized_end=1023
  _GETAPITOKENSREQUEST._serialized_start=1025
  _GETAPITOKENSREQUEST._serialized_end=1046
  _GETAPITOKENSRESPONSE._serialized_start=1048
  _GETAPITOKENSRESPONSE._serialized_end=1128
  _DELETEAPITOKENREQUEST._serialized_start=1130
  _DELETEAPITOKENREQUEST._serialized_end=1180
  _DELETEAPITOKENRESPONSE._serialized_start=1182
  _DELETEAPITOKENRESPONSE._serialized_end=1206
  _DELETEAPITOKENSREQUEST._serialized_start=1208
  _DELETEAPITOKENSREQUEST._serialized_end=1257
  _DELETEAPITOKENSRESPONSE._serialized_start=1259
  _DELETEAPITOKENSRESPONSE._serialized_end=1284
  _GETUSERREQUEST._serialized_start=1286
  _GETUSERREQUEST._serialized_end=1327
  _GETUSERRESPONSE._serialized_start=1330
  _GETUSERRESPONSE._serialized_end=1499
  _UPDATEUSERDISPLAYNAMEREQUEST._serialized_start=1501
  _UPDATEUSERDISPLAYNAMEREQUEST._serialized_end=1573
  _UPDATEUSERDISPLAYNAMERESPONSE._serialized_start=1575
  _UPDATEUSERDISPLAYNAMERESPONSE._serialized_end=1661
  _GETUSERPROJECTSREQUEST._serialized_start=1663
  _GETUSERPROJECTSREQUEST._serialized_end=1712
  _USERPROJECT._serialized_start=1714
  _USERPROJECT._serialized_end=1797
  _GETUSERPROJECTSRESPONSE._serialized_start=1799
  _GETUSERPROJECTSRESPONSE._serialized_end=1896
  _ACTIVATEUSERREQUEST._serialized_start=1899
  _ACTIVATEUSERREQUEST._serialized_end=2030
  _ACTIVATEUSERRESPONSE._serialized_start=2032
  _ACTIVATEUSERRESPONSE._serialized_end=2054
  _GETNOTACTIVATEDUSERSREQUEST._serialized_start=2056
  _GETNOTACTIVATEDUSERSREQUEST._serialized_end=2085
  _GETNOTACTIVATEDUSERSRESPONSE._serialized_start=2087
  _GETNOTACTIVATEDUSERSRESPONSE._serialized_end=2174
  _GETALLUSERSREQUEST._serialized_start=2176
  _GETALLUSERSREQUEST._serialized_end=2245
  _USERWITHPERMS._serialized_start=2248
  _USERWITHPERMS._serialized_end=2403
  _GETALLUSERSRESPONSE._serialized_start=2405
  _GETALLUSERSRESPONSE._serialized_end=2512
  _DEACTIVATEUSERREQUEST._serialized_start=2514
  _DEACTIVATEUSERREQUEST._serialized_end=2562
  _DEACTIVATEUSERRESPONSE._serialized_start=2564
  _DEACTIVATEUSERRESPONSE._serialized_end=2588
  _UPDATEUSEREMAILREQUEST._serialized_start=2590
  _UPDATEUSEREMAILREQUEST._serialized_end=2668
  _UPDATEUSEREMAILRESPONSE._serialized_start=2670
  _UPDATEUSEREMAILRESPONSE._serialized_end=2750
  _USERSERVICE._serialized_start=2753
  _USERSERVICE._serialized_end=4977
# @@protoc_insertion_point(module_scope)
