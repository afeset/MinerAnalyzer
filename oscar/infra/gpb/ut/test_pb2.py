# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/gpb/ut/test.proto',
  package='a.gpb.ut',
  serialized_pb='\n\x17infra/gpb/ut/test.proto\x12\x08\x61.gpb.ut\"%\n\tSimpleGpb\x12\x0b\n\x03int\x18\x01 \x01(\x03\x12\x0b\n\x03str\x18\x02 \x01(\t\"R\n\nStringsGpb\x12\x0c\n\x04str1\x18\n \x01(\t\x12\x0c\n\x04str2\x18\x14 \x01(\t\x12\x0c\n\x04str3\x18\x1e \x01(\t\x12\x0c\n\x04str4\x18( \x01(\t\x12\x0c\n\x04str5\x18\x32 \x01(\t\"S\n\x0bIntegersGpb\x12\x0c\n\x04int1\x18\x03 \x01(\x03\x12\x0c\n\x04int2\x18\x06 \x01(\x03\x12\x0c\n\x04int3\x18\t \x01(\x03\x12\x0c\n\x04int4\x18\x0c \x01(\x03\x12\x0c\n\x04int5\x18\x0f \x01(\x03')




_SIMPLEGPB = descriptor.Descriptor(
  name='SimpleGpb',
  full_name='a.gpb.ut.SimpleGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='int', full_name='a.gpb.ut.SimpleGpb.int', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str', full_name='a.gpb.ut.SimpleGpb.str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=37,
  serialized_end=74,
)


_STRINGSGPB = descriptor.Descriptor(
  name='StringsGpb',
  full_name='a.gpb.ut.StringsGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='str1', full_name='a.gpb.ut.StringsGpb.str1', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str2', full_name='a.gpb.ut.StringsGpb.str2', index=1,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str3', full_name='a.gpb.ut.StringsGpb.str3', index=2,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str4', full_name='a.gpb.ut.StringsGpb.str4', index=3,
      number=40, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str5', full_name='a.gpb.ut.StringsGpb.str5', index=4,
      number=50, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=76,
  serialized_end=158,
)


_INTEGERSGPB = descriptor.Descriptor(
  name='IntegersGpb',
  full_name='a.gpb.ut.IntegersGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='int1', full_name='a.gpb.ut.IntegersGpb.int1', index=0,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int2', full_name='a.gpb.ut.IntegersGpb.int2', index=1,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int3', full_name='a.gpb.ut.IntegersGpb.int3', index=2,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int4', full_name='a.gpb.ut.IntegersGpb.int4', index=3,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int5', full_name='a.gpb.ut.IntegersGpb.int5', index=4,
      number=15, type=3, cpp_type=2, label=1,
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
  serialized_start=160,
  serialized_end=243,
)



class SimpleGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SIMPLEGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.SimpleGpb)

class StringsGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STRINGSGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.StringsGpb)

class IntegersGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INTEGERSGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.IntegersGpb)

# @@protoc_insertion_point(module_scope)
