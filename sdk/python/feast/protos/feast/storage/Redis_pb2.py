# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feast/storage/Redis.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'feast/storage/Redis.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.protos.feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x66\x65\x61st/storage/Redis.proto\x12\rfeast.storage\x1a\x17\x66\x65\x61st/types/Value.proto\"^\n\nRedisKeyV2\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x14\n\x0c\x65ntity_names\x18\x02 \x03(\t\x12)\n\rentity_values\x18\x03 \x03(\x0b\x32\x12.feast.types.ValueBU\n\x13\x66\x65\x61st.proto.storageB\nRedisProtoZ2github.com/feast-dev/feast/go/protos/feast/storageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feast.storage.Redis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023feast.proto.storageB\nRedisProtoZ2github.com/feast-dev/feast/go/protos/feast/storage'
  _globals['_REDISKEYV2']._serialized_start=69
  _globals['_REDISKEYV2']._serialized_end=163
# @@protoc_insertion_point(module_scope)
