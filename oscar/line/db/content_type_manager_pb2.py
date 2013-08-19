# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='line/db/content_type_manager.proto',
  package='a.line.db',
  serialized_pb='\n\"line/db/content_type_manager.proto\x12\ta.line.db\x1a&include/a/infra/prov/definitions.proto\"\xed\x03\n\x1a\x43ontentTypeDetailedInfoGpb\x12-\n\x02id\x18\x01 \x01(\rB!\x8a\xb5\x18\x1dNumeric index of content type\x12<\n\x07isVideo\x18\x02 \x01(\x08\x42+\x8a\xb5\x18\'Is the content type considered as video\x12W\n\tisOverLap\x18\x03 \x01(\x08\x42\x44\x8a\xb5\x18@Did we see more than one type with this content type name prefix\x12#\n\x04name\x18\x04 \x01(\tB\x15\x8a\xb5\x18\x11\x43ontent type name\x12<\n\x0clastSecMbSec\x18\x05 \x01(\x04\x42&\x8a\xb5\x18\"Last second rate MBs for this type\x12<\n\x0clastMinMbSec\x18\x06 \x01(\x04\x42&\x8a\xb5\x18\"Last minute rate MBs for this type\x12h\n\x11\x63umulativePortion\x18\x07 \x01(\x01\x42M\x8a\xb5\x18IPortion of this type of the entire video servers traffic since last clear\"^\n\x12\x43ontentTypeInfoGpb\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12\x37\n\x08\x64\x65tailed\x18\x02 \x01(\x0b\x32%.a.line.db.ContentTypeDetailedInfoGpb\"\xd7\x04\n#ContentTypeManager_GetStatisticsGpb\x12\x43\n\x02in\x18\x01 \x01(\x0b\x32\x37.a.line.db.ContentTypeManager_GetStatisticsGpb.SetupGpb\x12\x45\n\x03out\x18\x02 \x01(\x0b\x32\x38.a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb\x1a\xc4\x02\n\tResultGpb\x12/\n\x08typeInfo\x18\x01 \x03(\x0b\x32\x1d.a.line.db.ContentTypeInfoGpb\x12V\n\x14lastSecVidPercentSec\x18\x02 \x01(\x01\x42\x38\x8a\xb5\x18\x34Last second percentage of video within video servers\x12V\n\x14lastMinVidPercentMin\x18\x03 \x01(\x01\x42\x38\x8a\xb5\x18\x34Last minute percentage of video within video servers\x12V\n\x14\x63umulativeVidPercent\x18\x04 \x01(\x01\x42\x38\x8a\xb5\x18\x34\x63umulative  percentage of video within video servers\x1a\x34\n\x08SetupGpb\x12(\n\x1ashouldReturnDetailedOutput\x18\x01 \x01(\x08:\x04true:\'\x8a\xb5\x18#Get content type manager statistics\"\xa8\x01\n#ContentTypeManager_ClearCountersGpb\x12\x1b\n\x02in\x18\x01 \x01(\x0b\x32\x0f.a.prov.NullGpb\x12\x1c\n\x03out\x18\x02 \x01(\x0b\x32\x0f.a.prov.NullGpb:F\x8a\xb5\x18\x42\x43lear content type manager statistics without forgetting the types')




_CONTENTTYPEDETAILEDINFOGPB = descriptor.Descriptor(
  name='ContentTypeDetailedInfoGpb',
  full_name='a.line.db.ContentTypeDetailedInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='a.line.db.ContentTypeDetailedInfoGpb.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\035Numeric index of content type')),
    descriptor.FieldDescriptor(
      name='isVideo', full_name='a.line.db.ContentTypeDetailedInfoGpb.isVideo', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\'Is the content type considered as video')),
    descriptor.FieldDescriptor(
      name='isOverLap', full_name='a.line.db.ContentTypeDetailedInfoGpb.isOverLap', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030@Did we see more than one type with this content type name prefix')),
    descriptor.FieldDescriptor(
      name='name', full_name='a.line.db.ContentTypeDetailedInfoGpb.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\021Content type name')),
    descriptor.FieldDescriptor(
      name='lastSecMbSec', full_name='a.line.db.ContentTypeDetailedInfoGpb.lastSecMbSec', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\"Last second rate MBs for this type')),
    descriptor.FieldDescriptor(
      name='lastMinMbSec', full_name='a.line.db.ContentTypeDetailedInfoGpb.lastMinMbSec', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\"Last minute rate MBs for this type')),
    descriptor.FieldDescriptor(
      name='cumulativePortion', full_name='a.line.db.ContentTypeDetailedInfoGpb.cumulativePortion', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030IPortion of this type of the entire video servers traffic since last clear')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=583,
)


_CONTENTTYPEINFOGPB = descriptor.Descriptor(
  name='ContentTypeInfoGpb',
  full_name='a.line.db.ContentTypeInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='summary', full_name='a.line.db.ContentTypeInfoGpb.summary', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='detailed', full_name='a.line.db.ContentTypeInfoGpb.detailed', index=1,
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
  serialized_start=585,
  serialized_end=679,
)


_CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB = descriptor.Descriptor(
  name='ResultGpb',
  full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='typeInfo', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb.typeInfo', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastSecVidPercentSec', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb.lastSecVidPercentSec', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\0304Last second percentage of video within video servers')),
    descriptor.FieldDescriptor(
      name='lastMinVidPercentMin', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb.lastMinVidPercentMin', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\0304Last minute percentage of video within video servers')),
    descriptor.FieldDescriptor(
      name='cumulativeVidPercent', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb.cumulativeVidPercent', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\0304cumulative  percentage of video within video servers')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=862,
  serialized_end=1186,
)

_CONTENTTYPEMANAGER_GETSTATISTICSGPB_SETUPGPB = descriptor.Descriptor(
  name='SetupGpb',
  full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.SetupGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shouldReturnDetailedOutput', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.SetupGpb.shouldReturnDetailedOutput', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  serialized_start=1188,
  serialized_end=1240,
)

_CONTENTTYPEMANAGER_GETSTATISTICSGPB = descriptor.Descriptor(
  name='ContentTypeManager_GetStatisticsGpb',
  full_name='a.line.db.ContentTypeManager_GetStatisticsGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.line.db.ContentTypeManager_GetStatisticsGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB, _CONTENTTYPEMANAGER_GETSTATISTICSGPB_SETUPGPB, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030#Get content type manager statistics'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=682,
  serialized_end=1281,
)


_CONTENTTYPEMANAGER_CLEARCOUNTERSGPB = descriptor.Descriptor(
  name='ContentTypeManager_ClearCountersGpb',
  full_name='a.line.db.ContentTypeManager_ClearCountersGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.line.db.ContentTypeManager_ClearCountersGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.line.db.ContentTypeManager_ClearCountersGpb.out', index=1,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030BClear content type manager statistics without forgetting the types'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1284,
  serialized_end=1452,
)

import include.a.infra.prov.definitions_pb2

_CONTENTTYPEINFOGPB.fields_by_name['detailed'].message_type = _CONTENTTYPEDETAILEDINFOGPB
_CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB.fields_by_name['typeInfo'].message_type = _CONTENTTYPEINFOGPB
_CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB.containing_type = _CONTENTTYPEMANAGER_GETSTATISTICSGPB;
_CONTENTTYPEMANAGER_GETSTATISTICSGPB_SETUPGPB.containing_type = _CONTENTTYPEMANAGER_GETSTATISTICSGPB;
_CONTENTTYPEMANAGER_GETSTATISTICSGPB.fields_by_name['in'].message_type = _CONTENTTYPEMANAGER_GETSTATISTICSGPB_SETUPGPB
_CONTENTTYPEMANAGER_GETSTATISTICSGPB.fields_by_name['out'].message_type = _CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB
_CONTENTTYPEMANAGER_CLEARCOUNTERSGPB.fields_by_name['in'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB
_CONTENTTYPEMANAGER_CLEARCOUNTERSGPB.fields_by_name['out'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB

class ContentTypeDetailedInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTENTTYPEDETAILEDINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeDetailedInfoGpb)

class ContentTypeInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTENTTYPEINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeInfoGpb)

class ContentTypeManager_GetStatisticsGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class ResultGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTTYPEMANAGER_GETSTATISTICSGPB_RESULTGPB
    
    # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeManager_GetStatisticsGpb.ResultGpb)
  
  class SetupGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTTYPEMANAGER_GETSTATISTICSGPB_SETUPGPB
    
    # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeManager_GetStatisticsGpb.SetupGpb)
  DESCRIPTOR = _CONTENTTYPEMANAGER_GETSTATISTICSGPB
  
  # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeManager_GetStatisticsGpb)

class ContentTypeManager_ClearCountersGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CONTENTTYPEMANAGER_CLEARCOUNTERSGPB
  
  # @@protoc_insertion_point(class_scope:a.line.db.ContentTypeManager_ClearCountersGpb)

# @@protoc_insertion_point(module_scope)
