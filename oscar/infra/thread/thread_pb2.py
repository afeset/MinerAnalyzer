# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/thread/thread.proto',
  package='a.thread',
  serialized_pb='\n\x19infra/thread/thread.proto\x12\x08\x61.thread\"\x82\x03\n\x11GetThreadsInfoGpb\x12\x30\n\x02in\x18\x01 \x01(\x0b\x32$.a.thread.GetThreadsInfoGpb.EmptyGpb\x12:\n\x03out\x18\x02 \x01(\x0b\x32-.a.thread.GetThreadsInfoGpb.ThreadInfoListGpb\x1a\n\n\x08\x45mptyGpb\x1a\xf2\x01\n\x11ThreadInfoListGpb\x12L\n\x07threads\x18\x01 \x03(\x0b\x32;.a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb\x1a\x8e\x01\n\rThreadInfoGpb\x12\x11\n\tshortName\x18\x01 \x01(\t\x12\x10\n\x08\x66ullName\x18\x02 \x01(\t\x12\x0b\n\x03tid\x18\x04 \x01(\x03\x12\x10\n\x08priority\x18\x05 \x01(\x03\x12\x0e\n\x06policy\x18\x08 \x01(\x03\x12\x14\n\x0c\x61\x66\x66inityMask\x18\x06 \x01(\x03\x12\x13\n\x0b\x63urrentCore\x18\x07 \x01(\x03')




_GETTHREADSINFOGPB_EMPTYGPB = descriptor.Descriptor(
  name='EmptyGpb',
  full_name='a.thread.GetThreadsInfoGpb.EmptyGpb',
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
  serialized_start=171,
  serialized_end=181,
)

_GETTHREADSINFOGPB_THREADINFOLISTGPB_THREADINFOGPB = descriptor.Descriptor(
  name='ThreadInfoGpb',
  full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shortName', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.shortName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fullName', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.fullName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tid', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.tid', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='priority', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.priority', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='policy', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.policy', index=4,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affinityMask', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.affinityMask', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='currentCore', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb.currentCore', index=6,
      number=7, type=3, cpp_type=2, label=1,
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
  serialized_start=284,
  serialized_end=426,
)

_GETTHREADSINFOGPB_THREADINFOLISTGPB = descriptor.Descriptor(
  name='ThreadInfoListGpb',
  full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='threads', full_name='a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.threads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETTHREADSINFOGPB_THREADINFOLISTGPB_THREADINFOGPB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=184,
  serialized_end=426,
)

_GETTHREADSINFOGPB = descriptor.Descriptor(
  name='GetThreadsInfoGpb',
  full_name='a.thread.GetThreadsInfoGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='in', full_name='a.thread.GetThreadsInfoGpb.in', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='out', full_name='a.thread.GetThreadsInfoGpb.out', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GETTHREADSINFOGPB_EMPTYGPB, _GETTHREADSINFOGPB_THREADINFOLISTGPB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=426,
)


_GETTHREADSINFOGPB_EMPTYGPB.containing_type = _GETTHREADSINFOGPB;
_GETTHREADSINFOGPB_THREADINFOLISTGPB_THREADINFOGPB.containing_type = _GETTHREADSINFOGPB_THREADINFOLISTGPB;
_GETTHREADSINFOGPB_THREADINFOLISTGPB.fields_by_name['threads'].message_type = _GETTHREADSINFOGPB_THREADINFOLISTGPB_THREADINFOGPB
_GETTHREADSINFOGPB_THREADINFOLISTGPB.containing_type = _GETTHREADSINFOGPB;
_GETTHREADSINFOGPB.fields_by_name['in'].message_type = _GETTHREADSINFOGPB_EMPTYGPB
_GETTHREADSINFOGPB.fields_by_name['out'].message_type = _GETTHREADSINFOGPB_THREADINFOLISTGPB

class GetThreadsInfoGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class EmptyGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GETTHREADSINFOGPB_EMPTYGPB
    
    # @@protoc_insertion_point(class_scope:a.thread.GetThreadsInfoGpb.EmptyGpb)
  
  class ThreadInfoListGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    
    class ThreadInfoGpb(message.Message):
      __metaclass__ = reflection.GeneratedProtocolMessageType
      DESCRIPTOR = _GETTHREADSINFOGPB_THREADINFOLISTGPB_THREADINFOGPB
      
      # @@protoc_insertion_point(class_scope:a.thread.GetThreadsInfoGpb.ThreadInfoListGpb.ThreadInfoGpb)
    DESCRIPTOR = _GETTHREADSINFOGPB_THREADINFOLISTGPB
    
    # @@protoc_insertion_point(class_scope:a.thread.GetThreadsInfoGpb.ThreadInfoListGpb)
  DESCRIPTOR = _GETTHREADSINFOGPB
  
  # @@protoc_insertion_point(class_scope:a.thread.GetThreadsInfoGpb)

# @@protoc_insertion_point(module_scope)