# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/prov/ut/basic.proto',
  package='a.prov.ut',
  serialized_pb='\n\x19infra/prov/ut/basic.proto\x12\ta.prov.ut\x1a google/protobuf/descriptor.proto\"7\n\x0eType1ConfigGpb\x12\x10\n\x05\x61ttr1\x18\x01 \x01(\x03:\x01\x37\x12\x13\n\x05\x61ttr2\x18\x02 \x01(\t:\x04lala\";\n\x12Type1BadConfigGpb1\x12\x10\n\x05\x61ttr1\x18\x01 \x02(\x03:\x01\x37\x12\x13\n\x05\x61ttr2\x18\x02 \x01(\t:\x04lala\"T\n\x12Type1BadConfigGpb2\x12\x10\n\x05\x61ttr1\x18\x01 \x01(\x03:\x01\x37\x12,\n\x05\x61ttr2\x18\x02 \x01(\x0b\x32\x1d.a.prov.ut.Type1BadConfigGpb1\"\x1d\n\x05InGpb\x12\t\n\x01\x61\x18\x01 \x01(\x03\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x15\n\x08GpbEmpty\x12\t\n\x01\x61\x18\x03 \x03(\x05\"#\n\x06OutGpb\x12\n\n\x02s3\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"H\n\x08\x46unnyGpb\x12\x1c\n\x02in\x18\x01 \x02(\x0b\x32\x10.a.prov.ut.InGpb\x12\x1e\n\x03out\x18\x02 \x02(\x0b\x32\x11.a.prov.ut.OutGpb\"&\n\x08SumInGpb\x12\x0c\n\x01\x61\x18\x01 \x01(\x03:\x01\x37\x12\x0c\n\x01\x62\x18\x02 \x01(\x03:\x01\x33\"%\n\tSumOutGpb\x12\t\n\x01\x63\x18\x01 \x01(\x03\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"L\n\x06SumGpb\x12\x1f\n\x02in\x18\x01 \x02(\x0b\x32\x13.a.prov.ut.SumInGpb\x12!\n\x03out\x18\x02 \x02(\x0b\x32\x14.a.prov.ut.SumOutGpb\"\xb3\x01\n\tConcatGpb\x12\'\n\x02in\x18\x01 \x02(\x0b\x32\x1b.a.prov.ut.ConcatGpb.InGpb1\x12)\n\x03out\x18\x02 \x02(\x0b\x32\x1c.a.prov.ut.ConcatGpb.OutGpb1\x1a,\n\x06InGpb1\x12\x10\n\x02s1\x18\x01 \x01(\t:\x04\x64\x65\x66\x31\x12\x10\n\x02s2\x18\x02 \x01(\t:\x04\x64\x65\x66\x32\x1a$\n\x07OutGpb1\x12\n\n\x02s3\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x03')




_TYPE1CONFIGGPB = descriptor.Descriptor(
  name='Type1ConfigGpb',
  full_name='a.prov.ut.Type1ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.prov.ut.Type1ConfigGpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.prov.ut.Type1ConfigGpb.attr2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("lala", "utf-8"),
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
  serialized_start=74,
  serialized_end=129,
)


_TYPE1BADCONFIGGPB1 = descriptor.Descriptor(
  name='Type1BadConfigGpb1',
  full_name='a.prov.ut.Type1BadConfigGpb1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.prov.ut.Type1BadConfigGpb1.attr1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.prov.ut.Type1BadConfigGpb1.attr2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("lala", "utf-8"),
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
  serialized_start=131,
  serialized_end=190,
)


_TYPE1BADCONFIGGPB2 = descriptor.Descriptor(
  name='Type1BadConfigGpb2',
  full_name='a.prov.ut.Type1BadConfigGpb2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.prov.ut.Type1BadConfigGpb2.attr1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.prov.ut.Type1BadConfigGpb2.attr2', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=192,
  serialized_end=276,
)


_INGPB = descriptor.Descriptor(
  name='InGpb',
  full_name='a.prov.ut.InGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='a.prov.ut.InGpb.a', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='a.prov.ut.InGpb.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=278,
  serialized_end=307,
)


_GPBEMPTY = descriptor.Descriptor(
  name='GpbEmpty',
  full_name='a.prov.ut.GpbEmpty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='a.prov.ut.GpbEmpty.a', index=0,
      number=3, type=5, cpp_type=1, label=3,
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
  serialized_start=309,
  serialized_end=330,
)


_OUTGPB = descriptor.Descriptor(
  name='OutGpb',
  full_name='a.prov.ut.OutGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='s3', full_name='a.prov.ut.OutGpb.s3', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='a.prov.ut.OutGpb.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=332,
  serialized_end=367,
)


_FUNNYGPB = descriptor.Descriptor(
  name='FunnyGpb',
  full_name='a.prov.ut.FunnyGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.prov.ut.FunnyGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.prov.ut.FunnyGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=369,
  serialized_end=441,
)


_SUMINGPB = descriptor.Descriptor(
  name='SumInGpb',
  full_name='a.prov.ut.SumInGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='a.prov.ut.SumInGpb.a', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='a.prov.ut.SumInGpb.b', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=3,
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
  serialized_start=443,
  serialized_end=481,
)


_SUMOUTGPB = descriptor.Descriptor(
  name='SumOutGpb',
  full_name='a.prov.ut.SumOutGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='c', full_name='a.prov.ut.SumOutGpb.c', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='a.prov.ut.SumOutGpb.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=483,
  serialized_end=520,
)


_SUMGPB = descriptor.Descriptor(
  name='SumGpb',
  full_name='a.prov.ut.SumGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.prov.ut.SumGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.prov.ut.SumGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=522,
  serialized_end=598,
)


_CONCATGPB_INGPB1 = descriptor.Descriptor(
  name='InGpb1',
  full_name='a.prov.ut.ConcatGpb.InGpb1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='s1', full_name='a.prov.ut.ConcatGpb.InGpb1.s1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("def1", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='s2', full_name='a.prov.ut.ConcatGpb.InGpb1.s2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("def2", "utf-8"),
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
  serialized_start=698,
  serialized_end=742,
)

_CONCATGPB_OUTGPB1 = descriptor.Descriptor(
  name='OutGpb1',
  full_name='a.prov.ut.ConcatGpb.OutGpb1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='s3', full_name='a.prov.ut.ConcatGpb.OutGpb1.s3', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='a.prov.ut.ConcatGpb.OutGpb1.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=744,
  serialized_end=780,
)

_CONCATGPB = descriptor.Descriptor(
  name='ConcatGpb',
  full_name='a.prov.ut.ConcatGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.prov.ut.ConcatGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.prov.ut.ConcatGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONCATGPB_INGPB1, _CONCATGPB_OUTGPB1, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=601,
  serialized_end=780,
)

import google.protobuf.descriptor_pb2

_TYPE1BADCONFIGGPB2.fields_by_name['attr2'].message_type = _TYPE1BADCONFIGGPB1
_FUNNYGPB.fields_by_name['in'].message_type = _INGPB
_FUNNYGPB.fields_by_name['out'].message_type = _OUTGPB
_SUMGPB.fields_by_name['in'].message_type = _SUMINGPB
_SUMGPB.fields_by_name['out'].message_type = _SUMOUTGPB
_CONCATGPB_INGPB1.containing_type = _CONCATGPB;
_CONCATGPB_OUTGPB1.containing_type = _CONCATGPB;
_CONCATGPB.fields_by_name['in'].message_type = _CONCATGPB_INGPB1
_CONCATGPB.fields_by_name['out'].message_type = _CONCATGPB_OUTGPB1

class Type1ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE1CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.Type1ConfigGpb)

class Type1BadConfigGpb1(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE1BADCONFIGGPB1
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.Type1BadConfigGpb1)

class Type1BadConfigGpb2(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE1BADCONFIGGPB2
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.Type1BadConfigGpb2)

class InGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.InGpb)

class GpbEmpty(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GPBEMPTY
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.GpbEmpty)

class OutGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OUTGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.OutGpb)

class FunnyGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FUNNYGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.FunnyGpb)

class SumInGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUMINGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.SumInGpb)

class SumOutGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUMOUTGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.SumOutGpb)

class SumGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SUMGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.SumGpb)

class ConcatGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class InGpb1(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONCATGPB_INGPB1
    
    # @@protoc_insertion_point(class_scope:a.prov.ut.ConcatGpb.InGpb1)
  
  class OutGpb1(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONCATGPB_OUTGPB1
    
    # @@protoc_insertion_point(class_scope:a.prov.ut.ConcatGpb.OutGpb1)
  DESCRIPTOR = _CONCATGPB
  
  # @@protoc_insertion_point(class_scope:a.prov.ut.ConcatGpb)

# @@protoc_insertion_point(module_scope)