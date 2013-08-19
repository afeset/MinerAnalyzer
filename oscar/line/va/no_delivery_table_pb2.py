# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='line/va/no_delivery_table.proto',
  package='a.line.va',
  serialized_pb='\n\x1fline/va/no_delivery_table.proto\x12\ta.line.va\x1a&include/a/infra/prov/definitions.proto\"\xde\x01\n\x17NoDeliveryTable_ShowGpb\x12\x31\n\x02in\x18\x01 \x01(\x0b\x32%.a.line.va.NoDeliveryTable_ShowGpb.In\x12\x33\n\x03out\x18\x02 \x01(\x0b\x32&.a.line.va.NoDeliveryTable_ShowGpb.Out\x1a\x18\n\x02In\x12\x12\n\x06\x66ilter\x18\x01 \x01(\t:\x02.*\x1a\x12\n\x03Out\x12\x0b\n\x03key\x18\x01 \x03(\t:-\x8a\xb5\x18)Show the content of the no delivery table')




_NODELIVERYTABLE_SHOWGPB_IN = descriptor.Descriptor(
  name='In',
  full_name='a.line.va.NoDeliveryTable_ShowGpb.In',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='filter', full_name='a.line.va.NoDeliveryTable_ShowGpb.In.filter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode(".*", "utf-8"),
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
  serialized_start=218,
  serialized_end=242,
)

_NODELIVERYTABLE_SHOWGPB_OUT = descriptor.Descriptor(
  name='Out',
  full_name='a.line.va.NoDeliveryTable_ShowGpb.Out',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='a.line.va.NoDeliveryTable_ShowGpb.Out.key', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=244,
  serialized_end=262,
)

_NODELIVERYTABLE_SHOWGPB = descriptor.Descriptor(
  name='NoDeliveryTable_ShowGpb',
  full_name='a.line.va.NoDeliveryTable_ShowGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.line.va.NoDeliveryTable_ShowGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.line.va.NoDeliveryTable_ShowGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NODELIVERYTABLE_SHOWGPB_IN, _NODELIVERYTABLE_SHOWGPB_OUT, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030)Show the content of the no delivery table'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=87,
  serialized_end=309,
)

import include.a.infra.prov.definitions_pb2

_NODELIVERYTABLE_SHOWGPB_IN.containing_type = _NODELIVERYTABLE_SHOWGPB;
_NODELIVERYTABLE_SHOWGPB_OUT.containing_type = _NODELIVERYTABLE_SHOWGPB;
_NODELIVERYTABLE_SHOWGPB.fields_by_name['in'].message_type = _NODELIVERYTABLE_SHOWGPB_IN
_NODELIVERYTABLE_SHOWGPB.fields_by_name['out'].message_type = _NODELIVERYTABLE_SHOWGPB_OUT

class NoDeliveryTable_ShowGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class In(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _NODELIVERYTABLE_SHOWGPB_IN
    
    # @@protoc_insertion_point(class_scope:a.line.va.NoDeliveryTable_ShowGpb.In)
  
  class Out(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _NODELIVERYTABLE_SHOWGPB_OUT
    
    # @@protoc_insertion_point(class_scope:a.line.va.NoDeliveryTable_ShowGpb.Out)
  DESCRIPTOR = _NODELIVERYTABLE_SHOWGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.NoDeliveryTable_ShowGpb)

# @@protoc_insertion_point(module_scope)
