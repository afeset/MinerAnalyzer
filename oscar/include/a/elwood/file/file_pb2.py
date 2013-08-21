# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/elwood/file/file.proto',
  package='a.elwood.file',
  serialized_pb='\n include/a/elwood/file/file.proto\x12\ra.elwood.file\x1a&include/a/infra/prov/definitions.proto\"\xad\x01\n\nGetInfoGpb\x12\x1b\n\x02in\x18\x01 \x01(\x0b\x32\x0f.a.prov.NullGpb\x12.\n\x03out\x18\x02 \x01(\x0b\x32!.a.elwood.file.GetInfoGpb.OutxGpb\x1a+\n\x07OutxGpb\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\x04:%\x8a\xb5\x18!Gets the file content information\"\xdd\x01\n\x0c\x43\x61lcCrc32Gpb\x12.\n\x02in\x18\x01 \x01(\x0b\x32\".a.elwood.file.CalcCrc32Gpb.InxGpb\x12\x30\n\x03out\x18\x02 \x01(\x0b\x32#.a.elwood.file.CalcCrc32Gpb.OutxGpb\x1a(\n\x06InxGpb\x12\x0e\n\x06length\x18\x01 \x01(\x04\x12\x0e\n\x06offset\x18\x02 \x01(\x04\x1a\x18\n\x07OutxGpb\x12\r\n\x05\x63rc32\x18\x01 \x01(\r:\'\x8a\xb5\x18#Calculates CRC32of the file content')




_GETINFOGPB_OUTXGPB = descriptor.Descriptor(
  name='OutxGpb',
  full_name='a.elwood.file.GetInfoGpb.OutxGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='filename', full_name='a.elwood.file.GetInfoGpb.OutxGpb.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='length', full_name='a.elwood.file.GetInfoGpb.OutxGpb.length', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=183,
  serialized_end=226,
)

_GETINFOGPB = descriptor.Descriptor(
  name='GetInfoGpb',
  full_name='a.elwood.file.GetInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.elwood.file.GetInfoGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.elwood.file.GetInfoGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETINFOGPB_OUTXGPB, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030!Gets the file content information'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=92,
  serialized_end=265,
)


_CALCCRC32GPB_INXGPB = descriptor.Descriptor(
  name='InxGpb',
  full_name='a.elwood.file.CalcCrc32Gpb.InxGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='length', full_name='a.elwood.file.CalcCrc32Gpb.InxGpb.length', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='a.elwood.file.CalcCrc32Gpb.InxGpb.offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=382,
  serialized_end=422,
)

_CALCCRC32GPB_OUTXGPB = descriptor.Descriptor(
  name='OutxGpb',
  full_name='a.elwood.file.CalcCrc32Gpb.OutxGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='crc32', full_name='a.elwood.file.CalcCrc32Gpb.OutxGpb.crc32', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=424,
  serialized_end=448,
)

_CALCCRC32GPB = descriptor.Descriptor(
  name='CalcCrc32Gpb',
  full_name='a.elwood.file.CalcCrc32Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.elwood.file.CalcCrc32Gpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.elwood.file.CalcCrc32Gpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CALCCRC32GPB_INXGPB, _CALCCRC32GPB_OUTXGPB, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030#Calculates CRC32of the file content'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=268,
  serialized_end=489,
)

import include.a.infra.prov.definitions_pb2

_GETINFOGPB_OUTXGPB.containing_type = _GETINFOGPB;
_GETINFOGPB.fields_by_name['in'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB
_GETINFOGPB.fields_by_name['out'].message_type = _GETINFOGPB_OUTXGPB
_CALCCRC32GPB_INXGPB.containing_type = _CALCCRC32GPB;
_CALCCRC32GPB_OUTXGPB.containing_type = _CALCCRC32GPB;
_CALCCRC32GPB.fields_by_name['in'].message_type = _CALCCRC32GPB_INXGPB
_CALCCRC32GPB.fields_by_name['out'].message_type = _CALCCRC32GPB_OUTXGPB

class GetInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class OutxGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GETINFOGPB_OUTXGPB
    
    # @@protoc_insertion_point(class_scope:a.elwood.file.GetInfoGpb.OutxGpb)
  DESCRIPTOR = _GETINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.elwood.file.GetInfoGpb)

class CalcCrc32Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class InxGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CALCCRC32GPB_INXGPB
    
    # @@protoc_insertion_point(class_scope:a.elwood.file.CalcCrc32Gpb.InxGpb)
  
  class OutxGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CALCCRC32GPB_OUTXGPB
    
    # @@protoc_insertion_point(class_scope:a.elwood.file.CalcCrc32Gpb.OutxGpb)
  DESCRIPTOR = _CALCCRC32GPB
  
  # @@protoc_insertion_point(class_scope:a.elwood.file.CalcCrc32Gpb)

# @@protoc_insertion_point(module_scope)