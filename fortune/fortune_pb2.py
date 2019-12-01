# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fortune.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fortune.proto',
  package='fortune',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rfortune.proto\x12\x07\x66ortune\"\x07\n\x05\x45mpty\" \n\x0e\x43ookieResponse\x12\x0e\n\x06\x63ookie\x18\x01 \x01(\t\"!\n\rCookieRequest\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\" \n\nCategories\x12\x12\n\ncategories\x18\x01 \x03(\t2\x82\x01\n\x07\x46ortune\x12\x37\n\x0eListCategories\x12\x0e.fortune.Empty\x1a\x13.fortune.Categories\"\x00\x12>\n\tGetCookie\x12\x16.fortune.CookieRequest\x1a\x17.fortune.CookieResponse\"\x00\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='fortune.Empty',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=33,
)


_COOKIERESPONSE = _descriptor.Descriptor(
  name='CookieResponse',
  full_name='fortune.CookieResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cookie', full_name='fortune.CookieResponse.cookie', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=67,
)


_COOKIEREQUEST = _descriptor.Descriptor(
  name='CookieRequest',
  full_name='fortune.CookieRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='fortune.CookieRequest.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=102,
)


_CATEGORIES = _descriptor.Descriptor(
  name='Categories',
  full_name='fortune.Categories',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='categories', full_name='fortune.Categories.categories', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['CookieResponse'] = _COOKIERESPONSE
DESCRIPTOR.message_types_by_name['CookieRequest'] = _COOKIEREQUEST
DESCRIPTOR.message_types_by_name['Categories'] = _CATEGORIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'fortune_pb2'
  # @@protoc_insertion_point(class_scope:fortune.Empty)
  })
_sym_db.RegisterMessage(Empty)

CookieResponse = _reflection.GeneratedProtocolMessageType('CookieResponse', (_message.Message,), {
  'DESCRIPTOR' : _COOKIERESPONSE,
  '__module__' : 'fortune_pb2'
  # @@protoc_insertion_point(class_scope:fortune.CookieResponse)
  })
_sym_db.RegisterMessage(CookieResponse)

CookieRequest = _reflection.GeneratedProtocolMessageType('CookieRequest', (_message.Message,), {
  'DESCRIPTOR' : _COOKIEREQUEST,
  '__module__' : 'fortune_pb2'
  # @@protoc_insertion_point(class_scope:fortune.CookieRequest)
  })
_sym_db.RegisterMessage(CookieRequest)

Categories = _reflection.GeneratedProtocolMessageType('Categories', (_message.Message,), {
  'DESCRIPTOR' : _CATEGORIES,
  '__module__' : 'fortune_pb2'
  # @@protoc_insertion_point(class_scope:fortune.Categories)
  })
_sym_db.RegisterMessage(Categories)



_FORTUNE = _descriptor.ServiceDescriptor(
  name='Fortune',
  full_name='fortune.Fortune',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=139,
  serialized_end=269,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListCategories',
    full_name='fortune.Fortune.ListCategories',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_CATEGORIES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetCookie',
    full_name='fortune.Fortune.GetCookie',
    index=1,
    containing_service=None,
    input_type=_COOKIEREQUEST,
    output_type=_COOKIERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FORTUNE)

DESCRIPTOR.services_by_name['Fortune'] = _FORTUNE

# @@protoc_insertion_point(module_scope)
