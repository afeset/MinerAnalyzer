# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='line/va/acquisition_controller.proto',
  package='a.line.va',
  serialized_pb='\n$line/va/acquisition_controller.proto\x12\ta.line.va\x1a&include/a/infra/prov/definitions.proto\"\xca\x0e\n\x10\x41\x63qm_GetStateGpb\x12\x1b\n\x02in\x18\x01 \x01(\x0b\x32\x0f.a.prov.NullGpb\x12,\n\x03out\x18\x02 \x01(\x0b\x32\x1f.a.line.va.Acqm_GetStateGpb.Out\x1a\xe4\x03\n\x07Session\x12\x32\n\x08\x66ileName\x18\x01 \x01(\tB \x8a\xb5\x18\x1c\x46ile name of current session\x12\x1a\n\x02id\x18\x02 \x01(\x03\x42\x0e\x8a\xb5\x18\nSession Id\x12\x0b\n\x03\x63id\x18\x03 \x01(\x04\x12\x34\n\x06length\x18\x04 \x01(\x03\x42$\x8a\xb5\x18 Expected session length in bytes\x12;\n\racquiredBytes\x18\x05 \x01(\x03\x42$\x8a\xb5\x18 Number of acquired bytes, so far\x12\x0e\n\x06\x63idHex\x18\x06 \x01(\t\x12j\n\x1eshouldDeallocateOnZeroRefCount\x18\x07 \x01(\x08\x42\x42\x8a\xb5\x18>Whether session will be deallocated when ref counter will be 0\x12O\n\x14wasContentFileOpened\x18\x08 \x01(\x08\x42\x31\x8a\xb5\x18-Whether content file is open for this session\x12<\n\x06refCnt\x18\t \x01(\x03\x42,\x8a\xb5\x18(Number of flows referencing this session\x1a\xf3\x02\n\x0f\x44iskWriterStats\x12\x1e\n\x06\x64iskId\x18\x01 \x01(\x03\x42\x0e\x8a\xb5\x18\ndisk index\x12\x46\n\x14\x63urrWriterQueueDepth\x18\x02 \x01(\x03\x42(\x8a\xb5\x18$Current num messages in writer queue\x12\x43\n\x14peakWriterQueueDepth\x18\x03 \x01(\x03\x42%\x8a\xb5\x18!Peak num messages in writer queue\x12Z\n\x12\x63urrNumAcqSessions\x18\x04 \x01(\x03\x42>\x8a\xb5\x18:Current number of acquisition sessions opened to this disk\x12W\n\x12peakNumAcqSessions\x18\x05 \x01(\x03\x42;\x8a\xb5\x18\x37Peak number of acquisition sessions opened to this disk\x1a\xf2\x06\n\x03Out\x12>\n\x14numSessionsAllocated\x18\x01 \x01(\x03\x42 \x8a\xb5\x18\x1cNumber of sessions allocated\x12\x34\n\x0c\x63urrSessions\x18\x02 \x01(\x03\x42\x1e\x8a\xb5\x18\x1a\x43urrent number of sessions\x12\x31\n\x0cpeakSessions\x18\x03 \x01(\x03\x42\x1b\x8a\xb5\x18\x17Peak number of sessions\x12\x46\n\x14\x63urrWriterQueueDepth\x18\x04 \x01(\x03\x42(\x8a\xb5\x18$Current num messages in writer queue\x12\x43\n\x14peakWriterQueueDepth\x18\x05 \x01(\x03\x42%\x8a\xb5\x18!Peak num messages in writer queue\x12W\n\x08sessions\x18\x06 \x03(\x0b\x32#.a.line.va.Acqm_GetStateGpb.SessionB \x8a\xb5\x18\x1c\x43urrent acquisition sessions\x12\x64\n\x0f\x64iskWriterStats\x18\x07 \x03(\x0b\x32+.a.line.va.Acqm_GetStateGpb.DiskWriterStatsB\x1e\x8a\xb5\x18\x1aper writer thread counters\x12\x45\n\x1amaxConcurrentSessionsLimit\x18\x08 \x01(\x03\x42!\x8a\xb5\x18\x1dMax concurrent sessions limit\x12\x96\x01\n-isNewSessionsAllowedBasedOnMetaDataDiskLimits\x18\t \x01(\x08\x42_\x8a\xb5\x18[Specifies if creation of new session is allowed based on current usage of metadata RAM disk\x12\x95\x01\n*isNewSessionsAllowedBasedOnMediaDiskLimits\x18\n \x03(\x08\x42\x61\x8a\xb5\x18]Specifies if creation of new session is allowed based on current usage of specific media disk:\x19\x8a\xb5\x18\x15Get the current state\"\xa1\x01\n\x11\x41\x63qm_DiskUsageGpb\x12\x17\n\x02id\x18\x01 \x01(\x04\x42\x0b\x8a\xb5\x18\x07\x64isk Id\x12\x38\n\x0etotalUsedBytes\x18\x02 \x01(\x04\x42 \x8a\xb5\x18\x1cNumber of used bytes, so far\x12\x39\n\x0etotalDiskBytes\x18\x03 \x01(\x04\x42!\x8a\xb5\x18\x1dNumber of total bytes on disk\"\x8d\x07\n\x15\x41\x63quisitionSummaryGpb\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x11\n\tsessionid\x18\x02 \x01(\x04\x12\x17\n\x0fmyAcquiredBytes\x18\x03 \x01(\x04\x12\x1c\n\x14myBrokenBytesSkipped\x18\x04 \x01(\x04\x12\x18\n\x10myLoggedClinetIp\x18\x05 \x01(\r\x12\x1a\n\x12myLoggedClinetPort\x18\x06 \x01(\r\x12\x18\n\x10myLoggedServerIp\x18\x07 \x01(\r\x12\x1a\n\x12myLoggedServerPort\x18\x08 \x01(\r\x12\x1c\n\x14wasContentFileOpened\x18\t \x01(\x08\x12\'\n\x1f\x41\x63qEndBadFailedCloseContentFile\x18\n \x01(\x08\x12(\n AcqEndBadFailedRemoveContentFile\x18\x0b \x01(\x08\x12/\n\'AcqEndBadFailedCloseExistingContentFile\x18\x0c \x01(\x08\x12#\n\x1b\x41\x63qEndBadContentFileNotOpen\x18\r \x01(\x08\x12\x1b\n\x13\x41\x63qEndSessionBroken\x18\x0e \x01(\x08\x12\x1b\n\x13\x41\x63qEndBadCscPartial\x18\x0f \x01(\x08\x12*\n\"AcqEndBadSessionCompleteFailNotify\x18\x10 \x01(\x08\x12!\n\x19\x41\x63qEndGoodSessionComplete\x18\x11 \x01(\x08\x12\"\n\x1a\x41\x63qEndBadSessionInComplete\x18\x12 \x01(\x08\x12#\n\x1b\x41\x63qEndGoodSessionInComplete\x18\x13 \x01(\x08\x12\x1b\n\x13\x41\x63qEndBadCscNotDone\x18\x14 \x01(\x08\x12\x17\n\x0f\x41\x63qEndNoNewData\x18\x15 \x01(\x08\x12#\n\x1b\x41\x63qEndBadFailedCreatingMeta\x18\x16 \x01(\x08\x12#\n\x1b\x41\x63qEndBadFailedUpdatingMeta\x18\x17 \x01(\x08\x12\x12\n\nAcqEndGood\x18\x18 \x01(\x08\x12\x1b\n\x13\x41\x63qEndCreateBadFile\x18\x19 \x01(\x08\x12\"\n\x1a\x41\x63qEndRemoveDataPersistent\x18\x1a \x01(\x08\x12\x1f\n\x17\x41\x63qEndNotKeepingContent\x18\x1b \x01(\x08\x12\"\n\x1a\x41\x63qEndErrorRemovingAcqFile\x18\x1c \x01(\x08\"\xcb\x01\n\x14\x41\x63quisitionConfigGpb\x12\x1b\n\x13sessionLowWaterMark\x18\x01 \x01(\x03\x12\x1c\n\x14sessionHighWaterMark\x18\x02 \x01(\x03\x12\x1c\n\x14numAllocatedSessions\x18\x03 \x01(\x03\x12\x1d\n\x15maxConcurrentSessions\x18\x04 \x01(\x03\x12\x1a\n\x12openFileInSyncMode\x18\x05 \x01(\x08\x12\x1f\n\x17predictionDiskSizeBytes\x18\x06 \x01(\x03\"y\n\x11\x41\x63qm_GetConfigGpb\x12\x1b\n\x02in\x18\x01 \x01(\x0b\x32\x0f.a.prov.NullGpb\x12,\n\x03out\x18\x02 \x01(\x0b\x32\x1f.a.line.va.AcquisitionConfigGpb:\x19\x8a\xb5\x18\x15Get configured values')




_ACQM_GETSTATEGPB_SESSION = descriptor.Descriptor(
  name='Session',
  full_name='a.line.va.Acqm_GetStateGpb.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fileName', full_name='a.line.va.Acqm_GetStateGpb.Session.fileName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\034File name of current session')),
    descriptor.FieldDescriptor(
      name='id', full_name='a.line.va.Acqm_GetStateGpb.Session.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\nSession Id')),
    descriptor.FieldDescriptor(
      name='cid', full_name='a.line.va.Acqm_GetStateGpb.Session.cid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='length', full_name='a.line.va.Acqm_GetStateGpb.Session.length', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030 Expected session length in bytes')),
    descriptor.FieldDescriptor(
      name='acquiredBytes', full_name='a.line.va.Acqm_GetStateGpb.Session.acquiredBytes', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030 Number of acquired bytes, so far')),
    descriptor.FieldDescriptor(
      name='cidHex', full_name='a.line.va.Acqm_GetStateGpb.Session.cidHex', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shouldDeallocateOnZeroRefCount', full_name='a.line.va.Acqm_GetStateGpb.Session.shouldDeallocateOnZeroRefCount', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030>Whether session will be deallocated when ref counter will be 0')),
    descriptor.FieldDescriptor(
      name='wasContentFileOpened', full_name='a.line.va.Acqm_GetStateGpb.Session.wasContentFileOpened', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030-Whether content file is open for this session')),
    descriptor.FieldDescriptor(
      name='refCnt', full_name='a.line.va.Acqm_GetStateGpb.Session.refCnt', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030(Number of flows referencing this session')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=188,
  serialized_end=672,
)

_ACQM_GETSTATEGPB_DISKWRITERSTATS = descriptor.Descriptor(
  name='DiskWriterStats',
  full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='diskId', full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats.diskId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\ndisk index')),
    descriptor.FieldDescriptor(
      name='currWriterQueueDepth', full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats.currWriterQueueDepth', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030$Current num messages in writer queue')),
    descriptor.FieldDescriptor(
      name='peakWriterQueueDepth', full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats.peakWriterQueueDepth', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030!Peak num messages in writer queue')),
    descriptor.FieldDescriptor(
      name='currNumAcqSessions', full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats.currNumAcqSessions', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030:Current number of acquisition sessions opened to this disk')),
    descriptor.FieldDescriptor(
      name='peakNumAcqSessions', full_name='a.line.va.Acqm_GetStateGpb.DiskWriterStats.peakNumAcqSessions', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\0307Peak number of acquisition sessions opened to this disk')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=675,
  serialized_end=1046,
)

_ACQM_GETSTATEGPB_OUT = descriptor.Descriptor(
  name='Out',
  full_name='a.line.va.Acqm_GetStateGpb.Out',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='numSessionsAllocated', full_name='a.line.va.Acqm_GetStateGpb.Out.numSessionsAllocated', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\034Number of sessions allocated')),
    descriptor.FieldDescriptor(
      name='currSessions', full_name='a.line.va.Acqm_GetStateGpb.Out.currSessions', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\032Current number of sessions')),
    descriptor.FieldDescriptor(
      name='peakSessions', full_name='a.line.va.Acqm_GetStateGpb.Out.peakSessions', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\027Peak number of sessions')),
    descriptor.FieldDescriptor(
      name='currWriterQueueDepth', full_name='a.line.va.Acqm_GetStateGpb.Out.currWriterQueueDepth', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030$Current num messages in writer queue')),
    descriptor.FieldDescriptor(
      name='peakWriterQueueDepth', full_name='a.line.va.Acqm_GetStateGpb.Out.peakWriterQueueDepth', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030!Peak num messages in writer queue')),
    descriptor.FieldDescriptor(
      name='sessions', full_name='a.line.va.Acqm_GetStateGpb.Out.sessions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\034Current acquisition sessions')),
    descriptor.FieldDescriptor(
      name='diskWriterStats', full_name='a.line.va.Acqm_GetStateGpb.Out.diskWriterStats', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\032per writer thread counters')),
    descriptor.FieldDescriptor(
      name='maxConcurrentSessionsLimit', full_name='a.line.va.Acqm_GetStateGpb.Out.maxConcurrentSessionsLimit', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\035Max concurrent sessions limit')),
    descriptor.FieldDescriptor(
      name='isNewSessionsAllowedBasedOnMetaDataDiskLimits', full_name='a.line.va.Acqm_GetStateGpb.Out.isNewSessionsAllowedBasedOnMetaDataDiskLimits', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030[Specifies if creation of new session is allowed based on current usage of metadata RAM disk')),
    descriptor.FieldDescriptor(
      name='isNewSessionsAllowedBasedOnMediaDiskLimits', full_name='a.line.va.Acqm_GetStateGpb.Out.isNewSessionsAllowedBasedOnMediaDiskLimits', index=9,
      number=10, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030]Specifies if creation of new session is allowed based on current usage of specific media disk')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1049,
  serialized_end=1931,
)

_ACQM_GETSTATEGPB = descriptor.Descriptor(
  name='Acqm_GetStateGpb',
  full_name='a.line.va.Acqm_GetStateGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.line.va.Acqm_GetStateGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.line.va.Acqm_GetStateGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ACQM_GETSTATEGPB_SESSION, _ACQM_GETSTATEGPB_DISKWRITERSTATS, _ACQM_GETSTATEGPB_OUT, ],
  enum_types=[
  ],
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030\025Get the current state'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=92,
  serialized_end=1958,
)


_ACQM_DISKUSAGEGPB = descriptor.Descriptor(
  name='Acqm_DiskUsageGpb',
  full_name='a.line.va.Acqm_DiskUsageGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='a.line.va.Acqm_DiskUsageGpb.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\007disk Id')),
    descriptor.FieldDescriptor(
      name='totalUsedBytes', full_name='a.line.va.Acqm_DiskUsageGpb.totalUsedBytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\034Number of used bytes, so far')),
    descriptor.FieldDescriptor(
      name='totalDiskBytes', full_name='a.line.va.Acqm_DiskUsageGpb.totalDiskBytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\212\265\030\035Number of total bytes on disk')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1961,
  serialized_end=2122,
)


_ACQUISITIONSUMMARYGPB = descriptor.Descriptor(
  name='AcquisitionSummaryGpb',
  full_name='a.line.va.AcquisitionSummaryGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cid', full_name='a.line.va.AcquisitionSummaryGpb.cid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionid', full_name='a.line.va.AcquisitionSummaryGpb.sessionid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myAcquiredBytes', full_name='a.line.va.AcquisitionSummaryGpb.myAcquiredBytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myBrokenBytesSkipped', full_name='a.line.va.AcquisitionSummaryGpb.myBrokenBytesSkipped', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myLoggedClinetIp', full_name='a.line.va.AcquisitionSummaryGpb.myLoggedClinetIp', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myLoggedClinetPort', full_name='a.line.va.AcquisitionSummaryGpb.myLoggedClinetPort', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myLoggedServerIp', full_name='a.line.va.AcquisitionSummaryGpb.myLoggedServerIp', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='myLoggedServerPort', full_name='a.line.va.AcquisitionSummaryGpb.myLoggedServerPort', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wasContentFileOpened', full_name='a.line.va.AcquisitionSummaryGpb.wasContentFileOpened', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadFailedCloseContentFile', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadFailedCloseContentFile', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadFailedRemoveContentFile', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadFailedRemoveContentFile', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadFailedCloseExistingContentFile', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadFailedCloseExistingContentFile', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadContentFileNotOpen', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadContentFileNotOpen', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndSessionBroken', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndSessionBroken', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadCscPartial', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadCscPartial', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadSessionCompleteFailNotify', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadSessionCompleteFailNotify', index=15,
      number=16, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndGoodSessionComplete', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndGoodSessionComplete', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadSessionInComplete', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadSessionInComplete', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndGoodSessionInComplete', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndGoodSessionInComplete', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadCscNotDone', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadCscNotDone', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndNoNewData', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndNoNewData', index=20,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadFailedCreatingMeta', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadFailedCreatingMeta', index=21,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndBadFailedUpdatingMeta', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndBadFailedUpdatingMeta', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndGood', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndGood', index=23,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndCreateBadFile', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndCreateBadFile', index=24,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndRemoveDataPersistent', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndRemoveDataPersistent', index=25,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndNotKeepingContent', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndNotKeepingContent', index=26,
      number=27, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='AcqEndErrorRemovingAcqFile', full_name='a.line.va.AcquisitionSummaryGpb.AcqEndErrorRemovingAcqFile', index=27,
      number=28, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=2125,
  serialized_end=3034,
)


_ACQUISITIONCONFIGGPB = descriptor.Descriptor(
  name='AcquisitionConfigGpb',
  full_name='a.line.va.AcquisitionConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sessionLowWaterMark', full_name='a.line.va.AcquisitionConfigGpb.sessionLowWaterMark', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionHighWaterMark', full_name='a.line.va.AcquisitionConfigGpb.sessionHighWaterMark', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='numAllocatedSessions', full_name='a.line.va.AcquisitionConfigGpb.numAllocatedSessions', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxConcurrentSessions', full_name='a.line.va.AcquisitionConfigGpb.maxConcurrentSessions', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='openFileInSyncMode', full_name='a.line.va.AcquisitionConfigGpb.openFileInSyncMode', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='predictionDiskSizeBytes', full_name='a.line.va.AcquisitionConfigGpb.predictionDiskSizeBytes', index=5,
      number=6, type=3, cpp_type=2, label=1,
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
  serialized_start=3037,
  serialized_end=3240,
)


_ACQM_GETCONFIGGPB = descriptor.Descriptor(
  name='Acqm_GetConfigGpb',
  full_name='a.line.va.Acqm_GetConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.line.va.Acqm_GetConfigGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.line.va.Acqm_GetConfigGpb.out', index=1,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\212\265\030\025Get configured values'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=3242,
  serialized_end=3363,
)

import include.a.infra.prov.definitions_pb2

_ACQM_GETSTATEGPB_SESSION.containing_type = _ACQM_GETSTATEGPB;
_ACQM_GETSTATEGPB_DISKWRITERSTATS.containing_type = _ACQM_GETSTATEGPB;
_ACQM_GETSTATEGPB_OUT.fields_by_name['sessions'].message_type = _ACQM_GETSTATEGPB_SESSION
_ACQM_GETSTATEGPB_OUT.fields_by_name['diskWriterStats'].message_type = _ACQM_GETSTATEGPB_DISKWRITERSTATS
_ACQM_GETSTATEGPB_OUT.containing_type = _ACQM_GETSTATEGPB;
_ACQM_GETSTATEGPB.fields_by_name['in'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB
_ACQM_GETSTATEGPB.fields_by_name['out'].message_type = _ACQM_GETSTATEGPB_OUT
_ACQM_GETCONFIGGPB.fields_by_name['in'].message_type = include.a.infra.prov.definitions_pb2._NULLGPB
_ACQM_GETCONFIGGPB.fields_by_name['out'].message_type = _ACQUISITIONCONFIGGPB

class Acqm_GetStateGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Session(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACQM_GETSTATEGPB_SESSION
    
    # @@protoc_insertion_point(class_scope:a.line.va.Acqm_GetStateGpb.Session)
  
  class DiskWriterStats(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACQM_GETSTATEGPB_DISKWRITERSTATS
    
    # @@protoc_insertion_point(class_scope:a.line.va.Acqm_GetStateGpb.DiskWriterStats)
  
  class Out(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ACQM_GETSTATEGPB_OUT
    
    # @@protoc_insertion_point(class_scope:a.line.va.Acqm_GetStateGpb.Out)
  DESCRIPTOR = _ACQM_GETSTATEGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.Acqm_GetStateGpb)

class Acqm_DiskUsageGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACQM_DISKUSAGEGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.Acqm_DiskUsageGpb)

class AcquisitionSummaryGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACQUISITIONSUMMARYGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.AcquisitionSummaryGpb)

class AcquisitionConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACQUISITIONCONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.AcquisitionConfigGpb)

class Acqm_GetConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACQM_GETCONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.line.va.Acqm_GetConfigGpb)

# @@protoc_insertion_point(module_scope)
