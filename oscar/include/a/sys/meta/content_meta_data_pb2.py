# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/sys/meta/content_meta_data.proto',
  package='a.sys.meta',
  serialized_pb='\n*include/a/sys/meta/content_meta_data.proto\x12\na.sys.meta\x1a&include/a/infra/prov/definitions.proto\"\xe4\x06\n\x12\x43ontentMetaDataGpb\x12\x13\n\x0b\x63ontentType\x18\x01 \x01(\t\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x0e\n\x06siteId\x18\x03 \x01(\x04\x12\x15\n\rcontentLength\x18\x04 \x01(\x03\x12\x17\n\x0fisFullyAcquired\x18\x05 \x01(\x08\x12\x37\n\x07segment\x18\x06 \x03(\x0b\x32&.a.sys.meta.ContentMetaDataGpb.Segment\x12\x15\n\rbytesAcquired\x18\x07 \x01(\x03\x12\x1d\n\x15mediaRelativeFilePath\x18\x08 \x01(\t\x12\x15\n\rbytesDiskSize\x18\t \x01(\x03\x12\x14\n\x0c\x63reationTime\x18\n \x01(\t\x12\x16\n\x0elastUpdateTime\x18\x0b \x01(\t\x12Q\n\x1csoftResponseValidationTokens\x18\x0c \x03(\x0b\x32+.a.sys.meta.ContentMetaDataGpb.KeyValuePair\x12Q\n\x1chardResponseValidationTokens\x18\r \x03(\x0b\x32+.a.sys.meta.ContentMetaDataGpb.KeyValuePair\x12@\n\x0csubItemsInfo\x18\x0e \x03(\x0b\x32*.a.sys.meta.ContentMetaDataGpb.SubItemInfo\x12K\n\x0flocationByCdnId\x18\x0f \x03(\x0b\x32\x32.a.sys.meta.ContentMetaDataGpb.NumericKeyValuePair\x1a*\n\x0cKeyValuePair\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a\x31\n\x13NumericKeyValuePair\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\t\x1a.\n\x07Segment\x12\x13\n\x0bstartOffset\x18\x01 \x01(\x04\x12\x0e\n\x06length\x18\x02 \x01(\x04\x1ao\n\x0bSubItemInfo\x12\x0e\n\x06subCid\x18\x01 \x01(\x04\x12\x17\n\x0fisFullyAcquired\x18\x02 \x01(\x08\x12\x37\n\x07segment\x18\x03 \x01(\x0b\x32&.a.sys.meta.ContentMetaDataGpb.Segment')




_CONTENTMETADATAGPB_KEYVALUEPAIR = descriptor.Descriptor(
  name='KeyValuePair',
  full_name='a.sys.meta.ContentMetaDataGpb.KeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='a.sys.meta.ContentMetaDataGpb.KeyValuePair.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='a.sys.meta.ContentMetaDataGpb.KeyValuePair.value', index=1,
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
  serialized_start=713,
  serialized_end=755,
)

_CONTENTMETADATAGPB_NUMERICKEYVALUEPAIR = descriptor.Descriptor(
  name='NumericKeyValuePair',
  full_name='a.sys.meta.ContentMetaDataGpb.NumericKeyValuePair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='key', full_name='a.sys.meta.ContentMetaDataGpb.NumericKeyValuePair.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='a.sys.meta.ContentMetaDataGpb.NumericKeyValuePair.value', index=1,
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
  serialized_start=757,
  serialized_end=806,
)

_CONTENTMETADATAGPB_SEGMENT = descriptor.Descriptor(
  name='Segment',
  full_name='a.sys.meta.ContentMetaDataGpb.Segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='startOffset', full_name='a.sys.meta.ContentMetaDataGpb.Segment.startOffset', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='length', full_name='a.sys.meta.ContentMetaDataGpb.Segment.length', index=1,
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
  serialized_start=808,
  serialized_end=854,
)

_CONTENTMETADATAGPB_SUBITEMINFO = descriptor.Descriptor(
  name='SubItemInfo',
  full_name='a.sys.meta.ContentMetaDataGpb.SubItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='subCid', full_name='a.sys.meta.ContentMetaDataGpb.SubItemInfo.subCid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isFullyAcquired', full_name='a.sys.meta.ContentMetaDataGpb.SubItemInfo.isFullyAcquired', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='segment', full_name='a.sys.meta.ContentMetaDataGpb.SubItemInfo.segment', index=2,
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
  serialized_start=856,
  serialized_end=967,
)

_CONTENTMETADATAGPB = descriptor.Descriptor(
  name='ContentMetaDataGpb',
  full_name='a.sys.meta.ContentMetaDataGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='contentType', full_name='a.sys.meta.ContentMetaDataGpb.contentType', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='location', full_name='a.sys.meta.ContentMetaDataGpb.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='siteId', full_name='a.sys.meta.ContentMetaDataGpb.siteId', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentLength', full_name='a.sys.meta.ContentMetaDataGpb.contentLength', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isFullyAcquired', full_name='a.sys.meta.ContentMetaDataGpb.isFullyAcquired', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='segment', full_name='a.sys.meta.ContentMetaDataGpb.segment', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bytesAcquired', full_name='a.sys.meta.ContentMetaDataGpb.bytesAcquired', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='mediaRelativeFilePath', full_name='a.sys.meta.ContentMetaDataGpb.mediaRelativeFilePath', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bytesDiskSize', full_name='a.sys.meta.ContentMetaDataGpb.bytesDiskSize', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='creationTime', full_name='a.sys.meta.ContentMetaDataGpb.creationTime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lastUpdateTime', full_name='a.sys.meta.ContentMetaDataGpb.lastUpdateTime', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='softResponseValidationTokens', full_name='a.sys.meta.ContentMetaDataGpb.softResponseValidationTokens', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hardResponseValidationTokens', full_name='a.sys.meta.ContentMetaDataGpb.hardResponseValidationTokens', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='subItemsInfo', full_name='a.sys.meta.ContentMetaDataGpb.subItemsInfo', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='locationByCdnId', full_name='a.sys.meta.ContentMetaDataGpb.locationByCdnId', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTENTMETADATAGPB_KEYVALUEPAIR, _CONTENTMETADATAGPB_NUMERICKEYVALUEPAIR, _CONTENTMETADATAGPB_SEGMENT, _CONTENTMETADATAGPB_SUBITEMINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=99,
  serialized_end=967,
)

import include.a.infra.prov.definitions_pb2

_CONTENTMETADATAGPB_KEYVALUEPAIR.containing_type = _CONTENTMETADATAGPB;
_CONTENTMETADATAGPB_NUMERICKEYVALUEPAIR.containing_type = _CONTENTMETADATAGPB;
_CONTENTMETADATAGPB_SEGMENT.containing_type = _CONTENTMETADATAGPB;
_CONTENTMETADATAGPB_SUBITEMINFO.fields_by_name['segment'].message_type = _CONTENTMETADATAGPB_SEGMENT
_CONTENTMETADATAGPB_SUBITEMINFO.containing_type = _CONTENTMETADATAGPB;
_CONTENTMETADATAGPB.fields_by_name['segment'].message_type = _CONTENTMETADATAGPB_SEGMENT
_CONTENTMETADATAGPB.fields_by_name['softResponseValidationTokens'].message_type = _CONTENTMETADATAGPB_KEYVALUEPAIR
_CONTENTMETADATAGPB.fields_by_name['hardResponseValidationTokens'].message_type = _CONTENTMETADATAGPB_KEYVALUEPAIR
_CONTENTMETADATAGPB.fields_by_name['subItemsInfo'].message_type = _CONTENTMETADATAGPB_SUBITEMINFO
_CONTENTMETADATAGPB.fields_by_name['locationByCdnId'].message_type = _CONTENTMETADATAGPB_NUMERICKEYVALUEPAIR

class ContentMetaDataGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class KeyValuePair(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTMETADATAGPB_KEYVALUEPAIR
    
    # @@protoc_insertion_point(class_scope:a.sys.meta.ContentMetaDataGpb.KeyValuePair)
  
  class NumericKeyValuePair(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTMETADATAGPB_NUMERICKEYVALUEPAIR
    
    # @@protoc_insertion_point(class_scope:a.sys.meta.ContentMetaDataGpb.NumericKeyValuePair)
  
  class Segment(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTMETADATAGPB_SEGMENT
    
    # @@protoc_insertion_point(class_scope:a.sys.meta.ContentMetaDataGpb.Segment)
  
  class SubItemInfo(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _CONTENTMETADATAGPB_SUBITEMINFO
    
    # @@protoc_insertion_point(class_scope:a.sys.meta.ContentMetaDataGpb.SubItemInfo)
  DESCRIPTOR = _CONTENTMETADATAGPB
  
  # @@protoc_insertion_point(class_scope:a.sys.meta.ContentMetaDataGpb)

# @@protoc_insertion_point(module_scope)