# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client-server-rpcs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63lient-server-rpcs.proto\"\x17\n\x07\x45ntries\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"!\n\x0eServerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\x0e\x43lientResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2o\n\nRPCHandler\x12,\n\rPutEntriesRPC\x12\x08.Entries\x1a\x0f.ServerResponse\"\x00\x12\x33\n\rAckEntriesRPC\x12\x0f.ServerResponse\x1a\x0f.ClientResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client_server_rpcs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTRIES._serialized_start=28
  _ENTRIES._serialized_end=51
  _SERVERRESPONSE._serialized_start=53
  _SERVERRESPONSE._serialized_end=86
  _CLIENTRESPONSE._serialized_start=88
  _CLIENTRESPONSE._serialized_end=121
  _RPCHANDLER._serialized_start=123
  _RPCHANDLER._serialized_end=234
# @@protoc_insertion_point(module_scope)
