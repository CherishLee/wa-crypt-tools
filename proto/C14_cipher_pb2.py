# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: C14_cipher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proto.C14_cipher_version_pb2 as C14__cipher__version__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x43\x31\x34_cipher.proto\x1a\x18\x43\x31\x34_cipher_version.proto\"U\n\nC14_cipher\x12\x13\n\x0bkey_version\x18\x02 \x01(\x0c\x12\x13\n\x0bserver_salt\x18\x03 \x01(\x0c\x12\x11\n\tgoogle_id\x18\x04 \x01(\x0c\x12\n\n\x02IV\x18\x05 \x01(\x0c\x62\x06proto3')



_C14_CIPHER = DESCRIPTOR.message_types_by_name['C14_cipher']
C14_cipher = _reflection.GeneratedProtocolMessageType('C14_cipher', (_message.Message,), {
  'DESCRIPTOR' : _C14_CIPHER,
  '__module__' : 'C14_cipher_pb2'
  # @@protoc_insertion_point(class_scope:C14_cipher)
  })
_sym_db.RegisterMessage(C14_cipher)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _C14_CIPHER._serialized_start=46
  _C14_CIPHER._serialized_end=131
# @@protoc_insertion_point(module_scope)