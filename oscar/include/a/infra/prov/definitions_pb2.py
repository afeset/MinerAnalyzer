# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/prov/definitions.proto',
  package='a.prov',
  serialized_pb='\n&include/a/infra/prov/definitions.proto\x12\x06\x61.prov\x1a google/protobuf/descriptor.proto\"\t\n\x07NullGpb\"H\n\x0cManagedRcGpb\x12\x13\n\x08\x65ngineRc\x18\x01 \x01(\x03:\x01\x30\x12\x11\n\x06\x61pplRc\x18\x02 \x01(\x03:\x01\x30\x12\x10\n\x08\x65rrorsRc\x18\x03 \x03(\t:6\n\rFieldHelpText\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\t::\n\x11\x46ieldDisplayAsKey\x12\x1d.google.protobuf.FieldOptions\x18\xd2\x86\x03 \x01(\x08::\n\x0fMessageHelpText\x12\x1f.google.protobuf.MessageOptions\x18\xd1\x86\x03 \x01(\t')


FIELDHELPTEXT_FIELD_NUMBER = 50001
FieldHelpText = descriptor.FieldDescriptor(
  name='FieldHelpText', full_name='a.prov.FieldHelpText', index=0,
  number=50001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=unicode("", "utf-8"),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
FIELDDISPLAYASKEY_FIELD_NUMBER = 50002
FieldDisplayAsKey = descriptor.FieldDescriptor(
  name='FieldDisplayAsKey', full_name='a.prov.FieldDisplayAsKey', index=1,
  number=50002, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
MESSAGEHELPTEXT_FIELD_NUMBER = 50001
MessageHelpText = descriptor.FieldDescriptor(
  name='MessageHelpText', full_name='a.prov.MessageHelpText', index=2,
  number=50001, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=unicode("", "utf-8"),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_NULLGPB = descriptor.Descriptor(
  name='NullGpb',
  full_name='a.prov.NullGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=84,
  serialized_end=93,
)


_MANAGEDRCGPB = descriptor.Descriptor(
  name='ManagedRcGpb',
  full_name='a.prov.ManagedRcGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='engineRc', full_name='a.prov.ManagedRcGpb.engineRc', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='applRc', full_name='a.prov.ManagedRcGpb.applRc', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='errorsRc', full_name='a.prov.ManagedRcGpb.errorsRc', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=95,
  serialized_end=167,
)

import google.protobuf.descriptor_pb2


class NullGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _NULLGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.NullGpb)

class ManagedRcGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MANAGEDRCGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ManagedRcGpb)

google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(FieldHelpText)
google.protobuf.descriptor_pb2.FieldOptions.RegisterExtension(FieldDisplayAsKey)
google.protobuf.descriptor_pb2.MessageOptions.RegisterExtension(MessageHelpText)
# @@protoc_insertion_point(module_scope)
