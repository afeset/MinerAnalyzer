# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/log/view/ut/test_gpb.proto',
  package='a.log.view',
  serialized_pb='\n infra/log/view/ut/test_gpb.proto\x12\na.log.view\"\x19\n\nLogTestGpb\x12\x0b\n\x03num\x18\x01 \x01(\x03')




_LOGTESTGPB = descriptor.Descriptor(
  name='LogTestGpb',
  full_name='a.log.view.LogTestGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='num', full_name='a.log.view.LogTestGpb.num', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=48,
  serialized_end=73,
)



class LogTestGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGTESTGPB
  
  # @@protoc_insertion_point(class_scope:a.log.view.LogTestGpb)

# @@protoc_insertion_point(module_scope)