# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/log/bits/msg_dumper_config.proto',
  package='a.log',
  serialized_pb='\n0include/a/infra/log/bits/msg_dumper_config.proto\x12\x05\x61.log\x1a\x1finclude/a/infra/log/level.proto\"\x83\x05\n\x14MsgFieldDumperCfgGpb\x12\x44\n\ndumpFormat\x18\x01 \x01(\x0e\x32\".a.log.MsgFieldDumperCfgGpb.Format:\x0ckFormatBlank\x12P\n\rdumpSubFormat\x18\x02 \x01(\x0e\x32%.a.log.MsgFieldDumperCfgGpb.SubFormat:\x12kSubFormatStandard\x12\x10\n\x05width\x18\x03 \x01(\x03:\x01\x30\x12M\n\x0btrimToWidth\x18\x04 \x01(\x0e\x32-.a.log.MsgFieldDumperCfgGpb.TrimToWidthMethod:\tkTrimNone\x12\x19\n\nnoDecorate\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x10prefixDecoration\x18\x06 \x01(\t:\x00\x12\x1a\n\x10suffixDecoration\x18\x07 \x01(\t:\x00\"m\n\x06\x46ormat\x12\x10\n\x0ckFormatBlank\x10\x00\x12\x12\n\x0ekFormatNumeric\x10\x01\x12\x10\n\x0ckFormatShort\x10\x02\x12\x0f\n\x0bkFormatLong\x10\x03\x12\x1a\n\x16kFormatIsoCompactMicro\x10\x04\"m\n\tSubFormat\x12\x16\n\x12kSubFormatStandard\x10\x00\x12\x16\n\x12kSubFormatWithLine\x10\x01\x12\x1a\n\x16kSubFormatWithTimeZone\x10\x02\x12\x14\n\x10kSubFormatWithId\x10\x03\"A\n\x11TrimToWidthMethod\x12\r\n\tkTrimNone\x10\x00\x12\x0e\n\nkTrimRight\x10\x01\x12\r\n\tkTrimLeft\x10\x02\"x\n\x18MsgFieldDescriptorCfgGpb\x12\x17\n\x08isToDump\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x15\n\norderIndex\x18\x02 \x01(\x03:\x01\x30\x12,\n\x07\x64umpCfg\x18\x03 \x01(\x0b\x32\x1b.a.log.MsgFieldDumperCfgGpb\"\xa6\x02\n!MsgBodyFragmentDumperCommonCfgGpb\x12O\n\ndumperType\x18\x01 \x01(\x0e\x32\x33.a.log.MsgBodyFragmentDumperCommonCfgGpb.DumperType:\x06kBlank\x12<\n\x11logThresholdLevel\x18\x02 \x01(\x0e\x32\x15.a.log.LevelGpb.Value:\nkLastLevel\"r\n\nDumperType\x12\n\n\x06kBlank\x10\x00\x12\x0b\n\x07kBinary\x10\x01\x12\x0b\n\x07kAsText\x10\x02\x12\n\n\x06kAsHex\x10\x03\x12\x0f\n\x0bkHeaderOnly\x10\x04\x12\x0e\n\nkBackTrace\x10\x05\x12\x11\n\rkDetailedText\x10\x06\"^\n\"MsgBodyFragmentDumperDefaultCfgGpb\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperCommonCfgGpb\"]\n!MsgBodyFragmentDumperStringCfgGpb\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperCommonCfgGpb\"a\n%MsgBodyFragmentDumperStackTraceCfgGpb\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperCommonCfgGpb\"]\n!MsgBodyFragmentDumperBufferCfgGpb\x12\x38\n\x06\x63ommon\x18\x01 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperCommonCfgGpb\"\xb1\x04\n\x13MsgBodyDumperCfgGpb\x12I\n\x16\x64\x65\x66\x61ultFragmentDumpCfg\x18\x01 \x01(\x0b\x32).a.log.MsgBodyFragmentDumperDefaultCfgGpb\x12G\n\x15stringFragmentDumpCfg\x18\x02 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperStringCfgGpb\x12N\n\x18\x62\x61\x63kTraceFragmentDumpCfg\x18\x03 \x01(\x0b\x32,.a.log.MsgBodyFragmentDumperStackTraceCfgGpb\x12M\n\x1b\x62inaryBufferFragmentDumpCfg\x18\x04 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperBufferCfgGpb\x12P\n\x1eplainTextBufferFragmentDumpCfg\x18\x05 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperBufferCfgGpb\x12O\n\x1djsonTextBufferFragmentDumpCfg\x18\x06 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperBufferCfgGpb\x12\x44\n\x12gpbFragmentDumpCfg\x18\x07 \x01(\x0b\x32(.a.log.MsgBodyFragmentDumperBufferCfgGpb\"\xd1\r\n\x0fMsgDumperCfgGpb\x12/\n\x0b\x62odyDumpCfg\x18\x01 \x01(\x0b\x32\x1a.a.log.MsgBodyDumperCfgGpb\x12\x11\n\tisCsvMode\x18\x02 \x01(\x08\x12\x18\n\x10isSingleLineMode\x18\x03 \x01(\x08\x12\x39\n\x10\x62odyFieldDumpCfg\x18\n \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12:\n\x11linePrefixDumpCfg\x18\x0b \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x43\n\x1amsgIdSequenceNumberDumpCfg\x18\x0c \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x44\n\x1bglobalSequenceNumberDumpCfg\x18\r \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12@\n\x17msgIdDropCounterDumpCfg\x18\x0e \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x41\n\x18globalDropCounterDumpCfg\x18\x0f \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x44\n\x1bloggerRecursionDepthDumpCfg\x18\x10 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12I\n loggerChainReactionLengthDumpCfg\x18\x11 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12:\n\x11moduleNameDumpCfg\x18\x12 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x39\n\x10groupNameDumpCfg\x18\x13 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x34\n\x0bnameDumpCfg\x18\x14 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x32\n\tidDumpCfg\x18\x15 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x38\n\x0flogLevelDumpCfg\x18\x16 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12>\n\x15sourceFileNameDumpCfg\x18\x17 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12@\n\x17sourceLineNumberDumpCfg\x18\x18 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x42\n\x19sourceFunctionNameDumpCfg\x18\x19 \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12<\n\x13timeOfDayGmtDumpCfg\x18\x1a \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12?\n\x16timeOfDayOriginDumpCfg\x18\x1b \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x41\n\x18timeOfDayTimeZoneDumpCfg\x18\x1c \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12=\n\x14timeMonotonicDumpCfg\x18\x1d \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x37\n\x0eprocessDumpCfg\x18\x1e \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x36\n\rthreadDumpCfg\x18\x1f \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12H\n\x1fprocessThreadAndInstanceDumpCfg\x18  \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x38\n\x0finstanceDumpCfg\x18! \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12\x35\n\x0c\x65rrnoDumpCfg\x18\" \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb\x12:\n\x11kickNumberDumpCfg\x18# \x01(\x0b\x32\x1f.a.log.MsgFieldDescriptorCfgGpb')



_MSGFIELDDUMPERCFGGPB_FORMAT = descriptor.EnumDescriptor(
  name='Format',
  full_name='a.log.MsgFieldDumperCfgGpb.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kFormatBlank', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFormatNumeric', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFormatShort', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFormatLong', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFormatIsoCompactMicro', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=449,
  serialized_end=558,
)

_MSGFIELDDUMPERCFGGPB_SUBFORMAT = descriptor.EnumDescriptor(
  name='SubFormat',
  full_name='a.log.MsgFieldDumperCfgGpb.SubFormat',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kSubFormatStandard', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kSubFormatWithLine', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kSubFormatWithTimeZone', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kSubFormatWithId', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=560,
  serialized_end=669,
)

_MSGFIELDDUMPERCFGGPB_TRIMTOWIDTHMETHOD = descriptor.EnumDescriptor(
  name='TrimToWidthMethod',
  full_name='a.log.MsgFieldDumperCfgGpb.TrimToWidthMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kTrimNone', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kTrimRight', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kTrimLeft', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=671,
  serialized_end=736,
)

_MSGBODYFRAGMENTDUMPERCOMMONCFGGPB_DUMPERTYPE = descriptor.EnumDescriptor(
  name='DumperType',
  full_name='a.log.MsgBodyFragmentDumperCommonCfgGpb.DumperType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kBlank', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kBinary', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kAsText', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kAsHex', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kHeaderOnly', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kBackTrace', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kDetailedText', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1041,
  serialized_end=1155,
)


_MSGFIELDDUMPERCFGGPB = descriptor.Descriptor(
  name='MsgFieldDumperCfgGpb',
  full_name='a.log.MsgFieldDumperCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dumpFormat', full_name='a.log.MsgFieldDumperCfgGpb.dumpFormat', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dumpSubFormat', full_name='a.log.MsgFieldDumperCfgGpb.dumpSubFormat', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='width', full_name='a.log.MsgFieldDumperCfgGpb.width', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='trimToWidth', full_name='a.log.MsgFieldDumperCfgGpb.trimToWidth', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='noDecorate', full_name='a.log.MsgFieldDumperCfgGpb.noDecorate', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='prefixDecoration', full_name='a.log.MsgFieldDumperCfgGpb.prefixDecoration', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suffixDecoration', full_name='a.log.MsgFieldDumperCfgGpb.suffixDecoration', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSGFIELDDUMPERCFGGPB_FORMAT,
    _MSGFIELDDUMPERCFGGPB_SUBFORMAT,
    _MSGFIELDDUMPERCFGGPB_TRIMTOWIDTHMETHOD,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=93,
  serialized_end=736,
)


_MSGFIELDDESCRIPTORCFGGPB = descriptor.Descriptor(
  name='MsgFieldDescriptorCfgGpb',
  full_name='a.log.MsgFieldDescriptorCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='isToDump', full_name='a.log.MsgFieldDescriptorCfgGpb.isToDump', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='orderIndex', full_name='a.log.MsgFieldDescriptorCfgGpb.orderIndex', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dumpCfg', full_name='a.log.MsgFieldDescriptorCfgGpb.dumpCfg', index=2,
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
  serialized_start=738,
  serialized_end=858,
)


_MSGBODYFRAGMENTDUMPERCOMMONCFGGPB = descriptor.Descriptor(
  name='MsgBodyFragmentDumperCommonCfgGpb',
  full_name='a.log.MsgBodyFragmentDumperCommonCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='dumperType', full_name='a.log.MsgBodyFragmentDumperCommonCfgGpb.dumperType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='logThresholdLevel', full_name='a.log.MsgBodyFragmentDumperCommonCfgGpb.logThresholdLevel', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=54,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB_DUMPERTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=861,
  serialized_end=1155,
)


_MSGBODYFRAGMENTDUMPERDEFAULTCFGGPB = descriptor.Descriptor(
  name='MsgBodyFragmentDumperDefaultCfgGpb',
  full_name='a.log.MsgBodyFragmentDumperDefaultCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='common', full_name='a.log.MsgBodyFragmentDumperDefaultCfgGpb.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1157,
  serialized_end=1251,
)


_MSGBODYFRAGMENTDUMPERSTRINGCFGGPB = descriptor.Descriptor(
  name='MsgBodyFragmentDumperStringCfgGpb',
  full_name='a.log.MsgBodyFragmentDumperStringCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='common', full_name='a.log.MsgBodyFragmentDumperStringCfgGpb.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1253,
  serialized_end=1346,
)


_MSGBODYFRAGMENTDUMPERSTACKTRACECFGGPB = descriptor.Descriptor(
  name='MsgBodyFragmentDumperStackTraceCfgGpb',
  full_name='a.log.MsgBodyFragmentDumperStackTraceCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='common', full_name='a.log.MsgBodyFragmentDumperStackTraceCfgGpb.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1348,
  serialized_end=1445,
)


_MSGBODYFRAGMENTDUMPERBUFFERCFGGPB = descriptor.Descriptor(
  name='MsgBodyFragmentDumperBufferCfgGpb',
  full_name='a.log.MsgBodyFragmentDumperBufferCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='common', full_name='a.log.MsgBodyFragmentDumperBufferCfgGpb.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=1447,
  serialized_end=1540,
)


_MSGBODYDUMPERCFGGPB = descriptor.Descriptor(
  name='MsgBodyDumperCfgGpb',
  full_name='a.log.MsgBodyDumperCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='defaultFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.defaultFragmentDumpCfg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stringFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.stringFragmentDumpCfg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='backTraceFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.backTraceFragmentDumpCfg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='binaryBufferFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.binaryBufferFragmentDumpCfg', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='plainTextBufferFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.plainTextBufferFragmentDumpCfg', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='jsonTextBufferFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.jsonTextBufferFragmentDumpCfg', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gpbFragmentDumpCfg', full_name='a.log.MsgBodyDumperCfgGpb.gpbFragmentDumpCfg', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=1543,
  serialized_end=2104,
)


_MSGDUMPERCFGGPB = descriptor.Descriptor(
  name='MsgDumperCfgGpb',
  full_name='a.log.MsgDumperCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bodyDumpCfg', full_name='a.log.MsgDumperCfgGpb.bodyDumpCfg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isCsvMode', full_name='a.log.MsgDumperCfgGpb.isCsvMode', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isSingleLineMode', full_name='a.log.MsgDumperCfgGpb.isSingleLineMode', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bodyFieldDumpCfg', full_name='a.log.MsgDumperCfgGpb.bodyFieldDumpCfg', index=3,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='linePrefixDumpCfg', full_name='a.log.MsgDumperCfgGpb.linePrefixDumpCfg', index=4,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msgIdSequenceNumberDumpCfg', full_name='a.log.MsgDumperCfgGpb.msgIdSequenceNumberDumpCfg', index=5,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='globalSequenceNumberDumpCfg', full_name='a.log.MsgDumperCfgGpb.globalSequenceNumberDumpCfg', index=6,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='msgIdDropCounterDumpCfg', full_name='a.log.MsgDumperCfgGpb.msgIdDropCounterDumpCfg', index=7,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='globalDropCounterDumpCfg', full_name='a.log.MsgDumperCfgGpb.globalDropCounterDumpCfg', index=8,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loggerRecursionDepthDumpCfg', full_name='a.log.MsgDumperCfgGpb.loggerRecursionDepthDumpCfg', index=9,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loggerChainReactionLengthDumpCfg', full_name='a.log.MsgDumperCfgGpb.loggerChainReactionLengthDumpCfg', index=10,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='moduleNameDumpCfg', full_name='a.log.MsgDumperCfgGpb.moduleNameDumpCfg', index=11,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupNameDumpCfg', full_name='a.log.MsgDumperCfgGpb.groupNameDumpCfg', index=12,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nameDumpCfg', full_name='a.log.MsgDumperCfgGpb.nameDumpCfg', index=13,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='idDumpCfg', full_name='a.log.MsgDumperCfgGpb.idDumpCfg', index=14,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='logLevelDumpCfg', full_name='a.log.MsgDumperCfgGpb.logLevelDumpCfg', index=15,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourceFileNameDumpCfg', full_name='a.log.MsgDumperCfgGpb.sourceFileNameDumpCfg', index=16,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourceLineNumberDumpCfg', full_name='a.log.MsgDumperCfgGpb.sourceLineNumberDumpCfg', index=17,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sourceFunctionNameDumpCfg', full_name='a.log.MsgDumperCfgGpb.sourceFunctionNameDumpCfg', index=18,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeOfDayGmtDumpCfg', full_name='a.log.MsgDumperCfgGpb.timeOfDayGmtDumpCfg', index=19,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeOfDayOriginDumpCfg', full_name='a.log.MsgDumperCfgGpb.timeOfDayOriginDumpCfg', index=20,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeOfDayTimeZoneDumpCfg', full_name='a.log.MsgDumperCfgGpb.timeOfDayTimeZoneDumpCfg', index=21,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeMonotonicDumpCfg', full_name='a.log.MsgDumperCfgGpb.timeMonotonicDumpCfg', index=22,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='processDumpCfg', full_name='a.log.MsgDumperCfgGpb.processDumpCfg', index=23,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='threadDumpCfg', full_name='a.log.MsgDumperCfgGpb.threadDumpCfg', index=24,
      number=31, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='processThreadAndInstanceDumpCfg', full_name='a.log.MsgDumperCfgGpb.processThreadAndInstanceDumpCfg', index=25,
      number=32, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='instanceDumpCfg', full_name='a.log.MsgDumperCfgGpb.instanceDumpCfg', index=26,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='errnoDumpCfg', full_name='a.log.MsgDumperCfgGpb.errnoDumpCfg', index=27,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kickNumberDumpCfg', full_name='a.log.MsgDumperCfgGpb.kickNumberDumpCfg', index=28,
      number=35, type=11, cpp_type=10, label=1,
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
  serialized_start=2107,
  serialized_end=3852,
)

import include.a.infra.log.level_pb2

_MSGFIELDDUMPERCFGGPB.fields_by_name['dumpFormat'].enum_type = _MSGFIELDDUMPERCFGGPB_FORMAT
_MSGFIELDDUMPERCFGGPB.fields_by_name['dumpSubFormat'].enum_type = _MSGFIELDDUMPERCFGGPB_SUBFORMAT
_MSGFIELDDUMPERCFGGPB.fields_by_name['trimToWidth'].enum_type = _MSGFIELDDUMPERCFGGPB_TRIMTOWIDTHMETHOD
_MSGFIELDDUMPERCFGGPB_FORMAT.containing_type = _MSGFIELDDUMPERCFGGPB;
_MSGFIELDDUMPERCFGGPB_SUBFORMAT.containing_type = _MSGFIELDDUMPERCFGGPB;
_MSGFIELDDUMPERCFGGPB_TRIMTOWIDTHMETHOD.containing_type = _MSGFIELDDUMPERCFGGPB;
_MSGFIELDDESCRIPTORCFGGPB.fields_by_name['dumpCfg'].message_type = _MSGFIELDDUMPERCFGGPB
_MSGBODYFRAGMENTDUMPERCOMMONCFGGPB.fields_by_name['dumperType'].enum_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB_DUMPERTYPE
_MSGBODYFRAGMENTDUMPERCOMMONCFGGPB.fields_by_name['logThresholdLevel'].enum_type = include.a.infra.log.level_pb2._LEVELGPB_VALUE
_MSGBODYFRAGMENTDUMPERCOMMONCFGGPB_DUMPERTYPE.containing_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB;
_MSGBODYFRAGMENTDUMPERDEFAULTCFGGPB.fields_by_name['common'].message_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB
_MSGBODYFRAGMENTDUMPERSTRINGCFGGPB.fields_by_name['common'].message_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB
_MSGBODYFRAGMENTDUMPERSTACKTRACECFGGPB.fields_by_name['common'].message_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB
_MSGBODYFRAGMENTDUMPERBUFFERCFGGPB.fields_by_name['common'].message_type = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['defaultFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERDEFAULTCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['stringFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERSTRINGCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['backTraceFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERSTACKTRACECFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['binaryBufferFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERBUFFERCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['plainTextBufferFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERBUFFERCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['jsonTextBufferFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERBUFFERCFGGPB
_MSGBODYDUMPERCFGGPB.fields_by_name['gpbFragmentDumpCfg'].message_type = _MSGBODYFRAGMENTDUMPERBUFFERCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['bodyDumpCfg'].message_type = _MSGBODYDUMPERCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['bodyFieldDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['linePrefixDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['msgIdSequenceNumberDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['globalSequenceNumberDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['msgIdDropCounterDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['globalDropCounterDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['loggerRecursionDepthDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['loggerChainReactionLengthDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['moduleNameDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['groupNameDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['nameDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['idDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['logLevelDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['sourceFileNameDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['sourceLineNumberDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['sourceFunctionNameDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['timeOfDayGmtDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['timeOfDayOriginDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['timeOfDayTimeZoneDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['timeMonotonicDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['processDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['threadDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['processThreadAndInstanceDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['instanceDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['errnoDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB
_MSGDUMPERCFGGPB.fields_by_name['kickNumberDumpCfg'].message_type = _MSGFIELDDESCRIPTORCFGGPB

class MsgFieldDumperCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGFIELDDUMPERCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgFieldDumperCfgGpb)

class MsgFieldDescriptorCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGFIELDDESCRIPTORCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgFieldDescriptorCfgGpb)

class MsgBodyFragmentDumperCommonCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYFRAGMENTDUMPERCOMMONCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyFragmentDumperCommonCfgGpb)

class MsgBodyFragmentDumperDefaultCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYFRAGMENTDUMPERDEFAULTCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyFragmentDumperDefaultCfgGpb)

class MsgBodyFragmentDumperStringCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYFRAGMENTDUMPERSTRINGCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyFragmentDumperStringCfgGpb)

class MsgBodyFragmentDumperStackTraceCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYFRAGMENTDUMPERSTACKTRACECFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyFragmentDumperStackTraceCfgGpb)

class MsgBodyFragmentDumperBufferCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYFRAGMENTDUMPERBUFFERCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyFragmentDumperBufferCfgGpb)

class MsgBodyDumperCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGBODYDUMPERCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgBodyDumperCfgGpb)

class MsgDumperCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MSGDUMPERCFGGPB
  
  # @@protoc_insertion_point(class_scope:a.log.MsgDumperCfgGpb)

# @@protoc_insertion_point(module_scope)