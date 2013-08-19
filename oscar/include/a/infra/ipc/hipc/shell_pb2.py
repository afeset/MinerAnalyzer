# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/ipc/hipc/shell.proto',
  package='a.ipc',
  serialized_pb='\n$include/a/infra/ipc/hipc/shell.proto\x12\x05\x61.ipc\x1a&include/a/infra/prov/definitions.proto\x1a\x1finclude/a/infra/ipc/utils.proto\"\x84\x01\n\x11HipcServerInfoGpb\x12\"\n\x04info\x18\x01 \x01(\x0b\x32\x14.a.ipc.ServerInfoGpb\x12\r\n\x05state\x18\x02 \x01(\t\x12\x14\n\x0csessionCount\x18\x03 \x01(\x03\x12\x10\n\x08socketId\x18\x04 \x01(\x03\x12\x14\n\x0cmainThreadId\x18\x05 \x01(\x03\"p\n\x14getHipcServerInfoGpb\x12\x1b\n\x02in\x18\x01 \x01(\x0b\x32\x0f.a.prov.NullGpb\x12%\n\x03out\x18\x02 \x01(\x0b\x32\x18.a.ipc.HipcServerInfoGpb:\x14\x8a\xb5\x18\x10HIPC Server info')




_HIPCSERVERINFOGPB = descriptor.Descriptor(
  name='HipcServerInfoGpb',
  full_name='a.ipc.HipcServerInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='info', full_name='a.ipc.HipcServerInfoGpb.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='state', full_name='a.ipc.HipcServerInfoGpb.state', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionCount', full_name='a.ipc.HipcServerInfoGpb.sessionCount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='socketId', full_name='a.ipc.HipcServerInfoGpb.socketId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mainThreadId', full_name='a.ipc.HipcServerInfoGpb.mainThreadId', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=121,
  serialized_end=253,
)


_GETHIPCSERVERINFOGPB = descriptor.Descriptor(
  name='getHipcServerInfoGpb',
  full_name='a.ipc.getHipcServerInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.ipc.getHipcServerInfoGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.ipc.getHipcServerInfoGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030\020HIPC Server info'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=255,
  serialized_end=367,
)

import include.a.infra.prov.definitions_pb2
import include.a.infra.ipc.utils_pb2

_HIPCSERVERINFOGPB.fields_by_name['info'].message_type = include.a.infra.ipc.utils_pb2._SERVERINFOGPB
_GETHIPCSERVERINFOGPB.fields_by_name['in'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB
_GETHIPCSERVERINFOGPB.fields_by_name['out'].message_type = _HIPCSERVERINFOGPB

class HipcServerInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HIPCSERVERINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.ipc.HipcServerInfoGpb)

class getHipcServerInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETHIPCSERVERINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.ipc.getHipcServerInfoGpb)

# @@protoc_insertion_point(module_scope)
