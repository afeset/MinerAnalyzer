# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='sys/bdb/bdb_reader.proto',
  package='a.sys.bdb',
  serialized_pb='\n\x18sys/bdb/bdb_reader.proto\x12\ta.sys.bdb\x1a&include/a/infra/prov/definitions.proto\"\xf8\x01\n\x11\x42\x64\x62Reader_ReadGpb\x12\x31\n\x02in\x18\x01 \x01(\x0b\x32%.a.sys.bdb.BdbReader_ReadGpb.InParams\x12\x33\n\x03out\x18\x02 \x01(\x0b\x32&.a.sys.bdb.BdbReader_ReadGpb.OutParams\x1a/\n\x08InParams\x12#\n\x04path\x18\x01 \x01(\tB\x15\x8a\xb5\x18\x11Path to read from\x1a\x32\n\tOutParams\x12%\n\x04\x64\x61ta\x18\x01 \x01(\tB\x17\x8a\xb5\x18\x13\x46ound data, as text:\x16\x8a\xb5\x18\x12Read one BDB entry')




_BDBREADER_READGPB_INPARAMS = descriptor.Descriptor(
  name='InParams',
  full_name='a.sys.bdb.BdbReader_ReadGpb.InParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='path', full_name='a.sys.bdb.BdbReader_ReadGpb.InParams.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\021Path to read from')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=205,
  serialized_end=252,
)

_BDBREADER_READGPB_OUTPARAMS = descriptor.Descriptor(
  name='OutParams',
  full_name='a.sys.bdb.BdbReader_ReadGpb.OutParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data', full_name='a.sys.bdb.BdbReader_ReadGpb.OutParams.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\023Found data, as text')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=254,
  serialized_end=304,
)

_BDBREADER_READGPB = descriptor.Descriptor(
  name='BdbReader_ReadGpb',
  full_name='a.sys.bdb.BdbReader_ReadGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.sys.bdb.BdbReader_ReadGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.sys.bdb.BdbReader_ReadGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BDBREADER_READGPB_INPARAMS, _BDBREADER_READGPB_OUTPARAMS, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030\022Read one BDB entry'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=80,
  serialized_end=328,
)

import include.a.infra.prov.definitions_pb2

_BDBREADER_READGPB_INPARAMS.containing_type = _BDBREADER_READGPB;
_BDBREADER_READGPB_OUTPARAMS.containing_type = _BDBREADER_READGPB;
_BDBREADER_READGPB.fields_by_name['in'].message_type = _BDBREADER_READGPB_INPARAMS
_BDBREADER_READGPB.fields_by_name['out'].message_type = _BDBREADER_READGPB_OUTPARAMS

class BdbReader_ReadGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class InParams(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BDBREADER_READGPB_INPARAMS
    
    # @@protoc_insertion_point(class_scope:a.sys.bdb.BdbReader_ReadGpb.InParams)
  
  class OutParams(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _BDBREADER_READGPB_OUTPARAMS
    
    # @@protoc_insertion_point(class_scope:a.sys.bdb.BdbReader_ReadGpb.OutParams)
  DESCRIPTOR = _BDBREADER_READGPB
  
  # @@protoc_insertion_point(class_scope:a.sys.bdb.BdbReader_ReadGpb)

# @@protoc_insertion_point(module_scope)