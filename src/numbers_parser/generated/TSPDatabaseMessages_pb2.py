# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TSPDatabaseMessages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import numbers_parser.generated.TSPMessages_pb2 as TSPMessages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TSPDatabaseMessages.proto',
  package='TSP',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19TSPDatabaseMessages.proto\x12\x03TSP\x1a\x11TSPMessages.proto\"0\n\x0c\x44\x61tabaseData\x12 \n\x04\x64\x61ta\x18\x01 \x02(\x0b\x32\x12.TSP.DataReference\"\x9a\x01\n\x13\x44\x61tabaseDataArchive\x12\x1c\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x0e.TSP.Reference\x12\x19\n\x11\x61pp_relative_path\x18\x02 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x03 \x02(\t\x12\x0e\n\x06length\x18\x04 \x01(\x04\x12\x0c\n\x04hash\x18\x05 \x01(\r\x12\x16\n\x08sharable\x18\x06 \x02(\x08:\x04true\"\xa9\x01\n\x18\x44\x61tabaseImageDataArchive\x12\'\n\x05super\x18\x01 \x02(\x0b\x32\x18.TSP.DatabaseDataArchive\x12\x35\n\x04type\x18\x02 \x02(\x0e\x32\'.TSP.DatabaseImageDataArchive.ImageType\"-\n\tImageType\x12\x0b\n\x07unknown\x10\x00\x12\n\n\x06\x62itmap\x10\x01\x12\x07\n\x03pdf\x10\x02'
  ,
  dependencies=[TSPMessages__pb2.DESCRIPTOR,])



_DATABASEIMAGEDATAARCHIVE_IMAGETYPE = _descriptor.EnumDescriptor(
  name='ImageType',
  full_name='TSP.DatabaseImageDataArchive.ImageType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='unknown', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='bitmap', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='pdf', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=385,
  serialized_end=430,
)
_sym_db.RegisterEnumDescriptor(_DATABASEIMAGEDATAARCHIVE_IMAGETYPE)


_DATABASEDATA = _descriptor.Descriptor(
  name='DatabaseData',
  full_name='TSP.DatabaseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TSP.DatabaseData.data', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=101,
)


_DATABASEDATAARCHIVE = _descriptor.Descriptor(
  name='DatabaseDataArchive',
  full_name='TSP.DatabaseDataArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='TSP.DatabaseDataArchive.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_relative_path', full_name='TSP.DatabaseDataArchive.app_relative_path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='TSP.DatabaseDataArchive.display_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='length', full_name='TSP.DatabaseDataArchive.length', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='TSP.DatabaseDataArchive.hash', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sharable', full_name='TSP.DatabaseDataArchive.sharable', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=True,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=258,
)


_DATABASEIMAGEDATAARCHIVE = _descriptor.Descriptor(
  name='DatabaseImageDataArchive',
  full_name='TSP.DatabaseImageDataArchive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='super', full_name='TSP.DatabaseImageDataArchive.super', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='TSP.DatabaseImageDataArchive.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATABASEIMAGEDATAARCHIVE_IMAGETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=430,
)

_DATABASEDATA.fields_by_name['data'].message_type = TSPMessages__pb2._DATAREFERENCE
_DATABASEDATAARCHIVE.fields_by_name['data'].message_type = TSPMessages__pb2._REFERENCE
_DATABASEIMAGEDATAARCHIVE.fields_by_name['super'].message_type = _DATABASEDATAARCHIVE
_DATABASEIMAGEDATAARCHIVE.fields_by_name['type'].enum_type = _DATABASEIMAGEDATAARCHIVE_IMAGETYPE
_DATABASEIMAGEDATAARCHIVE_IMAGETYPE.containing_type = _DATABASEIMAGEDATAARCHIVE
DESCRIPTOR.message_types_by_name['DatabaseData'] = _DATABASEDATA
DESCRIPTOR.message_types_by_name['DatabaseDataArchive'] = _DATABASEDATAARCHIVE
DESCRIPTOR.message_types_by_name['DatabaseImageDataArchive'] = _DATABASEIMAGEDATAARCHIVE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatabaseData = _reflection.GeneratedProtocolMessageType('DatabaseData', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEDATA,
  '__module__' : 'TSPDatabaseMessages_pb2'
  # @@protoc_insertion_point(class_scope:TSP.DatabaseData)
  })
_sym_db.RegisterMessage(DatabaseData)

DatabaseDataArchive = _reflection.GeneratedProtocolMessageType('DatabaseDataArchive', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEDATAARCHIVE,
  '__module__' : 'TSPDatabaseMessages_pb2'
  # @@protoc_insertion_point(class_scope:TSP.DatabaseDataArchive)
  })
_sym_db.RegisterMessage(DatabaseDataArchive)

DatabaseImageDataArchive = _reflection.GeneratedProtocolMessageType('DatabaseImageDataArchive', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEIMAGEDATAARCHIVE,
  '__module__' : 'TSPDatabaseMessages_pb2'
  # @@protoc_insertion_point(class_scope:TSP.DatabaseImageDataArchive)
  })
_sym_db.RegisterMessage(DatabaseImageDataArchive)


# @@protoc_insertion_point(module_scope)
