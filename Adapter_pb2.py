# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Adapter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Adapter.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rAdapter.proto\")\n\x12StartAutoMLRequest\x12\x13\n\x0bprocessJson\x18\x01 \x01(\t\"g\n\x13StartAutoMLResponse\x12&\n\nreturnCode\x18\x01 \x01(\x0e\x32\x12.AdapterReturnCode\x12\x14\n\x0cstatusUpdate\x18\x02 \x01(\t\x12\x12\n\noutputJson\x18\x03 \x01(\t*\x9b\x01\n\x11\x41\x64\x61pterReturnCode\x12\x1f\n\x1b\x41\x44\x41PTER_RETURN_CODE_UNKNOWN\x10\x00\x12\x1f\n\x1b\x41\x44\x41PTER_RETURN_CODE_SUCCESS\x10\x01\x12%\n!ADAPTER_RETURN_CODE_STATUS_UPDATE\x10\x02\x12\x1d\n\x19\x41\x44\x41PTER_RETURN_CODE_ERROR\x10\x64\x32N\n\x0e\x41\x64\x61pterService\x12<\n\x0bStartAutoML\x12\x13.StartAutoMLRequest\x1a\x14.StartAutoMLResponse\"\x00\x30\x01\x62\x06proto3'
)

_ADAPTERRETURNCODE = _descriptor.EnumDescriptor(
  name='AdapterReturnCode',
  full_name='AdapterReturnCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADAPTER_RETURN_CODE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADAPTER_RETURN_CODE_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADAPTER_RETURN_CODE_STATUS_UPDATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADAPTER_RETURN_CODE_ERROR', index=3, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=166,
  serialized_end=321,
)
_sym_db.RegisterEnumDescriptor(_ADAPTERRETURNCODE)

AdapterReturnCode = enum_type_wrapper.EnumTypeWrapper(_ADAPTERRETURNCODE)
ADAPTER_RETURN_CODE_UNKNOWN = 0
ADAPTER_RETURN_CODE_SUCCESS = 1
ADAPTER_RETURN_CODE_STATUS_UPDATE = 2
ADAPTER_RETURN_CODE_ERROR = 100



_STARTAUTOMLREQUEST = _descriptor.Descriptor(
  name='StartAutoMLRequest',
  full_name='StartAutoMLRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='processJson', full_name='StartAutoMLRequest.processJson', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=58,
)


_STARTAUTOMLRESPONSE = _descriptor.Descriptor(
  name='StartAutoMLResponse',
  full_name='StartAutoMLResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='returnCode', full_name='StartAutoMLResponse.returnCode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statusUpdate', full_name='StartAutoMLResponse.statusUpdate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='outputJson', full_name='StartAutoMLResponse.outputJson', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=163,
)

_STARTAUTOMLRESPONSE.fields_by_name['returnCode'].enum_type = _ADAPTERRETURNCODE
DESCRIPTOR.message_types_by_name['StartAutoMLRequest'] = _STARTAUTOMLREQUEST
DESCRIPTOR.message_types_by_name['StartAutoMLResponse'] = _STARTAUTOMLRESPONSE
DESCRIPTOR.enum_types_by_name['AdapterReturnCode'] = _ADAPTERRETURNCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartAutoMLRequest = _reflection.GeneratedProtocolMessageType('StartAutoMLRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTAUTOMLREQUEST,
  '__module__' : 'Adapter_pb2'
  # @@protoc_insertion_point(class_scope:StartAutoMLRequest)
  })
_sym_db.RegisterMessage(StartAutoMLRequest)

StartAutoMLResponse = _reflection.GeneratedProtocolMessageType('StartAutoMLResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTAUTOMLRESPONSE,
  '__module__' : 'Adapter_pb2'
  # @@protoc_insertion_point(class_scope:StartAutoMLResponse)
  })
_sym_db.RegisterMessage(StartAutoMLResponse)



_ADAPTERSERVICE = _descriptor.ServiceDescriptor(
  name='AdapterService',
  full_name='AdapterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=323,
  serialized_end=401,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartAutoML',
    full_name='AdapterService.StartAutoML',
    index=0,
    containing_service=None,
    input_type=_STARTAUTOMLREQUEST,
    output_type=_STARTAUTOMLRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADAPTERSERVICE)

DESCRIPTOR.services_by_name['AdapterService'] = _ADAPTERSERVICE

# @@protoc_insertion_point(module_scope)
