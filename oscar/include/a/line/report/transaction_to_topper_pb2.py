# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/line/report/transaction_to_topper.proto',
  package='a.line.report',
  serialized_pb='\n1include/a/line/report/transaction_to_topper.proto\x12\ra.line.report\x1a&include/a/infra/prov/definitions.proto\"\x84\t\n\x16TransactionToTopperGpb\x12\x14\n\x0csrcIpAddress\x18\x1c \x01(\t\x12\x14\n\x0c\x64stIpAddress\x18\x1d \x01(\t\x12\x12\n\x07srcPort\x18\x03 \x01(\r:\x01\x30\x12\x12\n\x07\x64stPort\x18\x04 \x01(\r:\x01\x30\x12\x1e\n\x13numResponderL2Bytes\x18\x05 \x01(\x03:\x01\x30\x12$\n\x19numDownloadedContentBytes\x18\x06 \x01(\x03:\x01\x30\x12\x1b\n\x10\x64ownloadTimeMsec\x18\x07 \x01(\x03:\x01\x30\x12\x17\n\x0cviewTimeMsec\x18\x08 \x01(\x03:\x01\x30\x12\x18\n\rcontentLength\x18\t \x01(\x03:\x01\x30\x12\x1c\n\x11\x63ontentChecksum1K\x18\n \x01(\x03:\x01\x30\x12\x14\n\tcontentId\x18\x0b \x01(\x03:\x01\x30\x12\x19\n\x0e\x63ontentGroupId\x18\x0c \x01(\x03:\x01\x30\x12\x16\n\x0b\x62\x65ginOffset\x18\r \x01(\x03:\x01\x30\x12\x16\n\x0b\x63ontentType\x18\x0e \x01(\t:\x01N\x12\x0f\n\x04host\x18\x0f \x01(\t:\x01N\x12\x0f\n\x04path\x18\x10 \x01(\t:\x01N\x12\x19\n\nisCachable\x18\x11 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0bisDelivered\x18\x12 \x01(\x08:\x05\x66\x61lse\x12\x1c\n\risViewSession\x18\x13 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0fsessionHitcount\x18\x14 \x01(\x04:\x01\x30\x12\x18\n\runixStartTime\x18) \x01(\x04:\x01\x30\x12\x1b\n\x10httpRequestRange\x18\x17 \x01(\t:\x01N\x12\x1c\n\x11httpResponseRange\x18\x18 \x01(\t:\x01N\x12\x17\n\x0corigHostName\x18\x19 \x01(\t:\x01N\x12\x1c\n\rwasRedirected\x18\x1a \x01(\x08:\x05\x66\x61lse\x12\x11\n\x06origin\x18\x1b \x01(\t:\x01N\x12\x1d\n\x12initialBurstBwKbps\x18\x1e \x01(\x04:\x01\x30\x12\x1d\n\x12initialBurstSizeKB\x18\x1f \x01(\x04:\x01\x30\x12\x1a\n\x0fsustainedBwKbps\x18  \x01(\x04:\x01\x30\x12\x18\n\rsignatureName\x18! \x01(\t:\x01N\x12/\n$transactionNumDownloadedContentBytes\x18\" \x01(\x03:\x01\x30\x12&\n\x1btransactionDownloadTimeMsec\x18# \x01(\x03:\x01\x30\x12\x1d\n\x12transactionSegment\x18$ \x01(\x03:\x01\x30\x12\x10\n\x05\x63\x64nId\x18% \x01(\x03:\x01\x30\x12\x18\n\rllnwdLocation\x18& \x01(\t:\x01N\x12\x12\n\x07titleId\x18\' \x01(\x03:\x01\x30\x12\x14\n\tsessionId\x18( \x01(\x03:\x01\x30\x12\"\n\x17sessionIdExtractorIndex\x18* \x01(\x03:\x01\x30\x12\x17\n\ndebugFlags\x18+ \x01(\t:\x03\x30x0\"P\n\x17TransactionSegmentValue\x12\x0b\n\x07kMiddle\x10\x00\x12\n\n\x06kFirst\x10\x01\x12\t\n\x05kLast\x10\x02\x12\x11\n\rkFirstAndLast\x10\x03')



_TRANSACTIONTOTOPPERGPB_TRANSACTIONSEGMENTVALUE = descriptor.EnumDescriptor(
  name='TransactionSegmentValue',
  full_name='a.line.report.TransactionToTopperGpb.TransactionSegmentValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kMiddle', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFirst', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kLast', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kFirstAndLast', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1185,
  serialized_end=1265,
)


_TRANSACTIONTOTOPPERGPB = descriptor.Descriptor(
  name='TransactionToTopperGpb',
  full_name='a.line.report.TransactionToTopperGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='srcIpAddress', full_name='a.line.report.TransactionToTopperGpb.srcIpAddress', index=0,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dstIpAddress', full_name='a.line.report.TransactionToTopperGpb.dstIpAddress', index=1,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='srcPort', full_name='a.line.report.TransactionToTopperGpb.srcPort', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dstPort', full_name='a.line.report.TransactionToTopperGpb.dstPort', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='numResponderL2Bytes', full_name='a.line.report.TransactionToTopperGpb.numResponderL2Bytes', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='numDownloadedContentBytes', full_name='a.line.report.TransactionToTopperGpb.numDownloadedContentBytes', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='downloadTimeMsec', full_name='a.line.report.TransactionToTopperGpb.downloadTimeMsec', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='viewTimeMsec', full_name='a.line.report.TransactionToTopperGpb.viewTimeMsec', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentLength', full_name='a.line.report.TransactionToTopperGpb.contentLength', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentChecksum1K', full_name='a.line.report.TransactionToTopperGpb.contentChecksum1K', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentId', full_name='a.line.report.TransactionToTopperGpb.contentId', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentGroupId', full_name='a.line.report.TransactionToTopperGpb.contentGroupId', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='beginOffset', full_name='a.line.report.TransactionToTopperGpb.beginOffset', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='contentType', full_name='a.line.report.TransactionToTopperGpb.contentType', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='host', full_name='a.line.report.TransactionToTopperGpb.host', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='path', full_name='a.line.report.TransactionToTopperGpb.path', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isCachable', full_name='a.line.report.TransactionToTopperGpb.isCachable', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isDelivered', full_name='a.line.report.TransactionToTopperGpb.isDelivered', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isViewSession', full_name='a.line.report.TransactionToTopperGpb.isViewSession', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionHitcount', full_name='a.line.report.TransactionToTopperGpb.sessionHitcount', index=19,
      number=20, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unixStartTime', full_name='a.line.report.TransactionToTopperGpb.unixStartTime', index=20,
      number=41, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='httpRequestRange', full_name='a.line.report.TransactionToTopperGpb.httpRequestRange', index=21,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='httpResponseRange', full_name='a.line.report.TransactionToTopperGpb.httpResponseRange', index=22,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origHostName', full_name='a.line.report.TransactionToTopperGpb.origHostName', index=23,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wasRedirected', full_name='a.line.report.TransactionToTopperGpb.wasRedirected', index=24,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='origin', full_name='a.line.report.TransactionToTopperGpb.origin', index=25,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='initialBurstBwKbps', full_name='a.line.report.TransactionToTopperGpb.initialBurstBwKbps', index=26,
      number=30, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='initialBurstSizeKB', full_name='a.line.report.TransactionToTopperGpb.initialBurstSizeKB', index=27,
      number=31, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sustainedBwKbps', full_name='a.line.report.TransactionToTopperGpb.sustainedBwKbps', index=28,
      number=32, type=4, cpp_type=4, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signatureName', full_name='a.line.report.TransactionToTopperGpb.signatureName', index=29,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transactionNumDownloadedContentBytes', full_name='a.line.report.TransactionToTopperGpb.transactionNumDownloadedContentBytes', index=30,
      number=34, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transactionDownloadTimeMsec', full_name='a.line.report.TransactionToTopperGpb.transactionDownloadTimeMsec', index=31,
      number=35, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='transactionSegment', full_name='a.line.report.TransactionToTopperGpb.transactionSegment', index=32,
      number=36, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cdnId', full_name='a.line.report.TransactionToTopperGpb.cdnId', index=33,
      number=37, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='llnwdLocation', full_name='a.line.report.TransactionToTopperGpb.llnwdLocation', index=34,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("N", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='titleId', full_name='a.line.report.TransactionToTopperGpb.titleId', index=35,
      number=39, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionId', full_name='a.line.report.TransactionToTopperGpb.sessionId', index=36,
      number=40, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sessionIdExtractorIndex', full_name='a.line.report.TransactionToTopperGpb.sessionIdExtractorIndex', index=37,
      number=42, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='debugFlags', full_name='a.line.report.TransactionToTopperGpb.debugFlags', index=38,
      number=43, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("0x0", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TRANSACTIONTOTOPPERGPB_TRANSACTIONSEGMENTVALUE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=109,
  serialized_end=1265,
)

import include.a.infra.prov.definitions_pb2

_TRANSACTIONTOTOPPERGPB_TRANSACTIONSEGMENTVALUE.containing_type = _TRANSACTIONTOTOPPERGPB;

class TransactionToTopperGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TRANSACTIONTOTOPPERGPB
  
  # @@protoc_insertion_point(class_scope:a.line.report.TransactionToTopperGpb)

# @@protoc_insertion_point(module_scope)