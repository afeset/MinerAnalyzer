# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='build/example/module2/private_prot.proto',
  package='a.build_example.module2',
  serialized_pb='\n(build/example/module2/private_prot.proto\x12\x17\x61.build_example.module2\x1a&include/a/infra/prov/definitions.proto\x1a<include/a/build/example/module2/module2_prot_interface.proto\"o\n\x0f\x44ummyMessageGpb\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x42\n\x0einterSomething\x18\x03 \x01(\x0b\x32*.a.build_example.module2.DummyInterfaceGpb')




_DUMMYMESSAGEGPB = descriptor.Descriptor(
  name='DummyMessageGpb',
  full_name='a.build_example.module2.DummyMessageGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='a.build_example.module2.DummyMessageGpb.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='a.build_example.module2.DummyMessageGpb.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='interSomething', full_name='a.build_example.module2.DummyMessageGpb.interSomething', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=171,
  serialized_end=282,
)

import include.a.infra.prov.definitions_pb2
import include.a.build.example.module2.module2_prot_interface_pb2

_DUMMYMESSAGEGPB.fields_by_name['interSomething'].message_type = include.a.build.example.module2.module2_prot_interface_pb2._DUMMYINTERFACEGPB

class DummyMessageGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DUMMYMESSAGEGPB
  
  # @@protoc_insertion_point(class_scope:a.build_example.module2.DummyMessageGpb)

# @@protoc_insertion_point(module_scope)
