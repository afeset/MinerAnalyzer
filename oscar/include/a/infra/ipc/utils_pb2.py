# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/ipc/utils.proto',
  package='a.ipc',
  serialized_pb='\n\x1finclude/a/infra/ipc/utils.proto\x12\x05\x61.ipc\"\xb5\x01\n\rServerInfoGpb\x12\x37\n\x04type\x18\x01 \x01(\x0e\x32\".a.ipc.ServerInfoGpb.TransportType:\x05kIPv4\x12\x12\n\x04port\x18\x02 \x01(\x03:\x04\x38\x30\x30\x31\x12\x1a\n\x07\x61\x64\x64ress\x18\x03 \x01(\t:\t127.0.0.1\";\n\rTransportType\x12\t\n\x05kIPv4\x10\x01\x12\x11\n\rkDomainSocket\x10\x02\x12\x0c\n\x08kSmQueue\x10\x03')



_SERVERINFOGPB_TRANSPORTTYPE = descriptor.EnumDescriptor(
  name='TransportType',
  full_name='a.ipc.ServerInfoGpb.TransportType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kIPv4', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kDomainSocket', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kSmQueue', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=165,
  serialized_end=224,
)


_SERVERINFOGPB = descriptor.Descriptor(
  name='ServerInfoGpb',
  full_name='a.ipc.ServerInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='a.ipc.ServerInfoGpb.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='port', full_name='a.ipc.ServerInfoGpb.port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=8001,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='address', full_name='a.ipc.ServerInfoGpb.address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("127.0.0.1", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERINFOGPB_TRANSPORTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=224,
)


_SERVERINFOGPB.fields_by_name['type'].enum_type = _SERVERINFOGPB_TRANSPORTTYPE
_SERVERINFOGPB_TRANSPORTTYPE.containing_type = _SERVERINFOGPB;

class ServerInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SERVERINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.ipc.ServerInfoGpb)

# @@protoc_insertion_point(module_scope)