# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/gpb/ut/chain_example.proto',
  package='a.gpb.ut',
  serialized_pb='\n infra/gpb/ut/chain_example.proto\x12\x08\x61.gpb.ut\"#\n\tHeaderGpb\x12\x16\n\x0esequanceNumber\x18\x01 \x01(\x04\",\n\tCircleGpb\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\x12\t\n\x01r\x18\x03 \x01(\x03\">\n\x0cRectangleGpb\x12\n\n\x02x1\x18\x01 \x01(\x03\x12\n\n\x02y1\x18\x02 \x01(\x03\x12\n\n\x02x2\x18\x03 \x01(\x03\x12\n\n\x02y2\x18\x04 \x01(\x03\"-\n\x07TextGpb\x12\t\n\x01x\x18\x01 \x01(\x03\x12\t\n\x01y\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t')




_HEADERGPB = descriptor.Descriptor(
  name='HeaderGpb',
  full_name='a.gpb.ut.HeaderGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sequanceNumber', full_name='a.gpb.ut.HeaderGpb.sequanceNumber', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=46,
  serialized_end=81,
)


_CIRCLEGPB = descriptor.Descriptor(
  name='CircleGpb',
  full_name='a.gpb.ut.CircleGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='a.gpb.ut.CircleGpb.x', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='a.gpb.ut.CircleGpb.y', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='r', full_name='a.gpb.ut.CircleGpb.r', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=83,
  serialized_end=127,
)


_RECTANGLEGPB = descriptor.Descriptor(
  name='RectangleGpb',
  full_name='a.gpb.ut.RectangleGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x1', full_name='a.gpb.ut.RectangleGpb.x1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y1', full_name='a.gpb.ut.RectangleGpb.y1', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x2', full_name='a.gpb.ut.RectangleGpb.x2', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y2', full_name='a.gpb.ut.RectangleGpb.y2', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=129,
  serialized_end=191,
)


_TEXTGPB = descriptor.Descriptor(
  name='TextGpb',
  full_name='a.gpb.ut.TextGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='a.gpb.ut.TextGpb.x', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='a.gpb.ut.TextGpb.y', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='text', full_name='a.gpb.ut.TextGpb.text', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=193,
  serialized_end=238,
)



class HeaderGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADERGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.HeaderGpb)

class CircleGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CIRCLEGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.CircleGpb)

class RectangleGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RECTANGLEGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.RectangleGpb)

class TextGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TEXTGPB
  
  # @@protoc_insertion_point(class_scope:a.gpb.ut.TextGpb)

# @@protoc_insertion_point(module_scope)
