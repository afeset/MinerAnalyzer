# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/net/util/ip_subnet.proto',
  package='a.net.util',
  serialized_pb='\n(include/a/infra/net/util/ip_subnet.proto\x12\na.net.util\x1a&include/a/infra/prov/definitions.proto\x1a)include/a/infra/net/util/ip_address.proto\"H\n\x0bIPSubnetGpb\x12+\n\tipAddress\x18\x01 \x01(\x0b\x32\x18.a.net.util.IPAddressGpb\x12\x0c\n\x04mask\x18\x02 \x01(\r')




_IPSUBNETGPB = descriptor.Descriptor(
  name='IPSubnetGpb',
  full_name='a.net.util.IPSubnetGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ipAddress', full_name='a.net.util.IPSubnetGpb.ipAddress', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mask', full_name='a.net.util.IPSubnetGpb.mask', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=139,
  serialized_end=211,
)

import include.a.infra.prov.definitions_pb2
import include.a.infra.net.util.ip_address_pb2

_IPSUBNETGPB.fields_by_name['ipAddress'].message_type = include.a.infra.net.util.ip_address_pb2._IPADDRESSGPB

class IPSubnetGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IPSUBNETGPB
  
  # @@protoc_insertion_point(class_scope:a.net.util.IPSubnetGpb)

# @@protoc_insertion_point(module_scope)