from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='system.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0csystem.proto\"\x1b\n\x0b\x42\x61seMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\"k\n\nSysMessage\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x13\n\x0bused_memory\x18\x02 \x01(\x03\x12\x14\n\x0ctotal_memory\x18\x03 \x01(\x03\x12\x11\n\tcpu_usage\x18\x04 \x01(\x02\x12\x11\n\tssd_usage\x18\x05 \x01(\x02\x62\x06proto3'
)




_BASEMESSAGE = _descriptor.Descriptor(
  name='BaseMessage',
  full_name='BaseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='BaseMessage.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=43,
)


_SYSMESSAGE = _descriptor.Descriptor(
  name='SysMessage',
  full_name='SysMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='SysMessage.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='used_memory', full_name='SysMessage.used_memory', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_memory', full_name='SysMessage.total_memory', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_usage', full_name='SysMessage.cpu_usage', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ssd_usage', full_name='SysMessage.ssd_usage', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=45,
  serialized_end=152,
)

DESCRIPTOR.message_types_by_name['BaseMessage'] = _BASEMESSAGE
DESCRIPTOR.message_types_by_name['SysMessage'] = _SYSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BaseMessage = _reflection.GeneratedProtocolMessageType('BaseMessage', (_message.Message,), {
  'DESCRIPTOR' : _BASEMESSAGE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:BaseMessage)
  })
_sym_db.RegisterMessage(BaseMessage)

SysMessage = _reflection.GeneratedProtocolMessageType('SysMessage', (_message.Message,), {
  'DESCRIPTOR' : _SYSMESSAGE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:SysMessage)
  })
_sym_db.RegisterMessage(SysMessage)


# @@protoc_insertion_point(module_scope)
