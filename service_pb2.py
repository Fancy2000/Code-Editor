# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\"S\n\x11RegistrateRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07surname\x18\x04 \x01(\t\"O\n\x12RegistrateResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07surname\x18\x04 \x01(\t\"/\n\x0cLogInRequest\x12\r\n\x05login\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"J\n\rLogInResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04info\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07surname\x18\x04 \x01(\t\"&\n\x05Users\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\":\n\x0bListOfUsers\x12\x1d\n\rlist_of_users\x18\x01 \x03(\x0b\x32\x06.Users\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x07\n\x05\x45mpty\"2\n\x11WriteUserResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\"@\n\x11RoomIdLogResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07surname\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\"M\n\rRoomIdRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x0c\n\x04text\x18\x04 \x01(\t\"c\n\x10RoomIdLogRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\r\n\x05login\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\"N\n\x0eNewRoleRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07surname\x18\x03 \x01(\t\x12\x0c\n\x04role\x18\x04 \x01(\t\"\x1f\n\x0fNewRoleResponse\x12\x0c\n\x04role\x18\x01 \x01(\t2\xdc\x02\n\x07Message\x12.\n\x0eGetListOfUsers\x12\x0e.RoomIdRequest\x1a\x0c.ListOfUsers\x12\x37\n\x0cRegistration\x12\x12.RegistrateRequest\x1a\x13.RegistrateResponse\x12&\n\x05LogIn\x12\r.LogInRequest\x1a\x0e.LogInResponse\x12-\n\x0fGetUserWhoWrite\x12\x06.Empty\x1a\x12.WriteUserResponse\x12,\n\x0eSetUserWhWrite\x12\x12.WriteUserResponse\x1a\x06.Empty\x12\x32\n\tSetRoomId\x12\x11.RoomIdLogRequest\x1a\x12.RoomIdLogResponse\x12/\n\nUpdateRole\x12\x0f.NewRoleRequest\x1a\x10.NewRoleResponseb\x06proto3')



_REGISTRATEREQUEST = DESCRIPTOR.message_types_by_name['RegistrateRequest']
_REGISTRATERESPONSE = DESCRIPTOR.message_types_by_name['RegistrateResponse']
_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LogInRequest']
_LOGINRESPONSE = DESCRIPTOR.message_types_by_name['LogInResponse']
_USERS = DESCRIPTOR.message_types_by_name['Users']
_LISTOFUSERS = DESCRIPTOR.message_types_by_name['ListOfUsers']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
_WRITEUSERRESPONSE = DESCRIPTOR.message_types_by_name['WriteUserResponse']
_ROOMIDLOGRESPONSE = DESCRIPTOR.message_types_by_name['RoomIdLogResponse']
_ROOMIDREQUEST = DESCRIPTOR.message_types_by_name['RoomIdRequest']
_ROOMIDLOGREQUEST = DESCRIPTOR.message_types_by_name['RoomIdLogRequest']
_NEWROLEREQUEST = DESCRIPTOR.message_types_by_name['NewRoleRequest']
_NEWROLERESPONSE = DESCRIPTOR.message_types_by_name['NewRoleResponse']
RegistrateRequest = _reflection.GeneratedProtocolMessageType('RegistrateRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RegistrateRequest)
  })
_sym_db.RegisterMessage(RegistrateRequest)

RegistrateResponse = _reflection.GeneratedProtocolMessageType('RegistrateResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTRATERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RegistrateResponse)
  })
_sym_db.RegisterMessage(RegistrateResponse)

LogInRequest = _reflection.GeneratedProtocolMessageType('LogInRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:LogInRequest)
  })
_sym_db.RegisterMessage(LogInRequest)

LogInResponse = _reflection.GeneratedProtocolMessageType('LogInResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGINRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:LogInResponse)
  })
_sym_db.RegisterMessage(LogInResponse)

Users = _reflection.GeneratedProtocolMessageType('Users', (_message.Message,), {
  'DESCRIPTOR' : _USERS,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Users)
  })
_sym_db.RegisterMessage(Users)

ListOfUsers = _reflection.GeneratedProtocolMessageType('ListOfUsers', (_message.Message,), {
  'DESCRIPTOR' : _LISTOFUSERS,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:ListOfUsers)
  })
_sym_db.RegisterMessage(ListOfUsers)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

WriteUserResponse = _reflection.GeneratedProtocolMessageType('WriteUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITEUSERRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:WriteUserResponse)
  })
_sym_db.RegisterMessage(WriteUserResponse)

RoomIdLogResponse = _reflection.GeneratedProtocolMessageType('RoomIdLogResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROOMIDLOGRESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RoomIdLogResponse)
  })
_sym_db.RegisterMessage(RoomIdLogResponse)

RoomIdRequest = _reflection.GeneratedProtocolMessageType('RoomIdRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROOMIDREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RoomIdRequest)
  })
_sym_db.RegisterMessage(RoomIdRequest)

RoomIdLogRequest = _reflection.GeneratedProtocolMessageType('RoomIdLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROOMIDLOGREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:RoomIdLogRequest)
  })
_sym_db.RegisterMessage(RoomIdLogRequest)

NewRoleRequest = _reflection.GeneratedProtocolMessageType('NewRoleRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWROLEREQUEST,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:NewRoleRequest)
  })
_sym_db.RegisterMessage(NewRoleRequest)

NewRoleResponse = _reflection.GeneratedProtocolMessageType('NewRoleResponse', (_message.Message,), {
  'DESCRIPTOR' : _NEWROLERESPONSE,
  '__module__' : 'service_pb2'
  # @@protoc_insertion_point(class_scope:NewRoleResponse)
  })
_sym_db.RegisterMessage(NewRoleResponse)

_MESSAGE = DESCRIPTOR.services_by_name['Message']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTRATEREQUEST._serialized_start=17
  _REGISTRATEREQUEST._serialized_end=100
  _REGISTRATERESPONSE._serialized_start=102
  _REGISTRATERESPONSE._serialized_end=181
  _LOGINREQUEST._serialized_start=183
  _LOGINREQUEST._serialized_end=230
  _LOGINRESPONSE._serialized_start=232
  _LOGINRESPONSE._serialized_end=306
  _USERS._serialized_start=308
  _USERS._serialized_end=346
  _LISTOFUSERS._serialized_start=348
  _LISTOFUSERS._serialized_end=406
  _EMPTY._serialized_start=408
  _EMPTY._serialized_end=415
  _WRITEUSERRESPONSE._serialized_start=417
  _WRITEUSERRESPONSE._serialized_end=467
  _ROOMIDLOGRESPONSE._serialized_start=469
  _ROOMIDLOGRESPONSE._serialized_end=533
  _ROOMIDREQUEST._serialized_start=535
  _ROOMIDREQUEST._serialized_end=612
  _ROOMIDLOGREQUEST._serialized_start=614
  _ROOMIDLOGREQUEST._serialized_end=713
  _NEWROLEREQUEST._serialized_start=715
  _NEWROLEREQUEST._serialized_end=793
  _NEWROLERESPONSE._serialized_start=795
  _NEWROLERESPONSE._serialized_end=826
  _MESSAGE._serialized_start=829
  _MESSAGE._serialized_end=1177
# @@protoc_insertion_point(module_scope)