# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='sys/sim/system_instance_number.proto',
  package='a.sys.sim',
  serialized_pb='\n$sys/sim/system_instance_number.proto\x12\ta.sys.sim\"&\n\x17SystemInstanceNumberGpb\x12\x0b\n\x03num\x18\x01 \x01(\x03')




_SYSTEMINSTANCENUMBERGPB = descriptor.Descriptor(
  name='SystemInstanceNumberGpb',
  full_name='a.sys.sim.SystemInstanceNumberGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='num', full_name='a.sys.sim.SystemInstanceNumberGpb.num', index=0,
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
  serialized_start=51,
  serialized_end=89,
)



class SystemInstanceNumberGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SYSTEMINSTANCENUMBERGPB
  
  # @@protoc_insertion_point(class_scope:a.sys.sim.SystemInstanceNumberGpb)

# @@protoc_insertion_point(module_scope)