# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2/proto/agent.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow_v2/proto/agent.proto',
  package='google.cloud.dialogflow.v2',
  syntax='proto3',
  serialized_pb=_b('\n,google/cloud/dialogflow_v2/proto/agent.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xfd\x02\n\x05\x41gent\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ult_language_code\x18\x03 \x01(\t\x12 \n\x18supported_language_codes\x18\x04 \x03(\t\x12\x11\n\ttime_zone\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x12\n\navatar_uri\x18\x07 \x01(\t\x12\x16\n\x0e\x65nable_logging\x18\x08 \x01(\x08\x12?\n\nmatch_mode\x18\t \x01(\x0e\x32+.google.cloud.dialogflow.v2.Agent.MatchMode\x12 \n\x18\x63lassification_threshold\x18\n \x01(\x02\"V\n\tMatchMode\x12\x1a\n\x16MATCH_MODE_UNSPECIFIED\x10\x00\x12\x15\n\x11MATCH_MODE_HYBRID\x10\x01\x12\x16\n\x12MATCH_MODE_ML_ONLY\x10\x02\"!\n\x0fGetAgentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"L\n\x13SearchAgentsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"b\n\x14SearchAgentsResponse\x12\x31\n\x06\x61gents\x18\x01 \x03(\x0b\x32!.google.cloud.dialogflow.v2.Agent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"#\n\x11TrainAgentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\"7\n\x12\x45xportAgentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x11\n\tagent_uri\x18\x02 \x01(\t\"L\n\x13\x45xportAgentResponse\x12\x13\n\tagent_uri\x18\x01 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x02 \x01(\x0cH\x00\x42\x07\n\x05\x61gent\"[\n\x12ImportAgentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x13\n\tagent_uri\x18\x02 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x03 \x01(\x0cH\x00\x42\x07\n\x05\x61gent\"\\\n\x13RestoreAgentRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x13\n\tagent_uri\x18\x02 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x03 \x01(\x0cH\x00\x42\x07\n\x05\x61gent2\xee\x06\n\x06\x41gents\x12\x81\x01\n\x08GetAgent\x12+.google.cloud.dialogflow.v2.GetAgentRequest\x1a!.google.cloud.dialogflow.v2.Agent\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v2/{parent=projects/*}/agent\x12\x9f\x01\n\x0cSearchAgents\x12/.google.cloud.dialogflow.v2.SearchAgentsRequest\x1a\x30.google.cloud.dialogflow.v2.SearchAgentsResponse\",\x82\xd3\xe4\x93\x02&\x12$/v2/{parent=projects/*}/agent:search\x12\x8a\x01\n\nTrainAgent\x12-.google.cloud.dialogflow.v2.TrainAgentRequest\x1a\x1d.google.longrunning.Operation\".\x82\xd3\xe4\x93\x02(\"#/v2/{parent=projects/*}/agent:train:\x01*\x12\x8d\x01\n\x0b\x45xportAgent\x12..google.cloud.dialogflow.v2.ExportAgentRequest\x1a\x1d.google.longrunning.Operation\"/\x82\xd3\xe4\x93\x02)\"$/v2/{parent=projects/*}/agent:export:\x01*\x12\x8d\x01\n\x0bImportAgent\x12..google.cloud.dialogflow.v2.ImportAgentRequest\x1a\x1d.google.longrunning.Operation\"/\x82\xd3\xe4\x93\x02)\"$/v2/{parent=projects/*}/agent:import:\x01*\x12\x90\x01\n\x0cRestoreAgent\x12/.google.cloud.dialogflow.v2.RestoreAgentRequest\x1a\x1d.google.longrunning.Operation\"0\x82\xd3\xe4\x93\x02*\"%/v2/{parent=projects/*}/agent:restore:\x01*B\x99\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\nAgentProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_AGENT_MATCHMODE = _descriptor.EnumDescriptor(
  name='MatchMode',
  full_name='google.cloud.dialogflow.v2.Agent.MatchMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MATCH_MODE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATCH_MODE_HYBRID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MATCH_MODE_ML_ONLY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=532,
  serialized_end=618,
)
_sym_db.RegisterEnumDescriptor(_AGENT_MATCHMODE)


_AGENT = _descriptor.Descriptor(
  name='Agent',
  full_name='google.cloud.dialogflow.v2.Agent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.Agent.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.dialogflow.v2.Agent.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_language_code', full_name='google.cloud.dialogflow.v2.Agent.default_language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supported_language_codes', full_name='google.cloud.dialogflow.v2.Agent.supported_language_codes', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_zone', full_name='google.cloud.dialogflow.v2.Agent.time_zone', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.dialogflow.v2.Agent.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_uri', full_name='google.cloud.dialogflow.v2.Agent.avatar_uri', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_logging', full_name='google.cloud.dialogflow.v2.Agent.enable_logging', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_mode', full_name='google.cloud.dialogflow.v2.Agent.match_mode', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classification_threshold', full_name='google.cloud.dialogflow.v2.Agent.classification_threshold', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGENT_MATCHMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=618,
)


_GETAGENTREQUEST = _descriptor.Descriptor(
  name='GetAgentRequest',
  full_name='google.cloud.dialogflow.v2.GetAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.GetAgentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=620,
  serialized_end=653,
)


_SEARCHAGENTSREQUEST = _descriptor.Descriptor(
  name='SearchAgentsRequest',
  full_name='google.cloud.dialogflow.v2.SearchAgentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.SearchAgentsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2.SearchAgentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2.SearchAgentsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=655,
  serialized_end=731,
)


_SEARCHAGENTSRESPONSE = _descriptor.Descriptor(
  name='SearchAgentsResponse',
  full_name='google.cloud.dialogflow.v2.SearchAgentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agents', full_name='google.cloud.dialogflow.v2.SearchAgentsResponse.agents', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2.SearchAgentsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=831,
)


_TRAINAGENTREQUEST = _descriptor.Descriptor(
  name='TrainAgentRequest',
  full_name='google.cloud.dialogflow.v2.TrainAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.TrainAgentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=833,
  serialized_end=868,
)


_EXPORTAGENTREQUEST = _descriptor.Descriptor(
  name='ExportAgentRequest',
  full_name='google.cloud.dialogflow.v2.ExportAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.ExportAgentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_uri', full_name='google.cloud.dialogflow.v2.ExportAgentRequest.agent_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=870,
  serialized_end=925,
)


_EXPORTAGENTRESPONSE = _descriptor.Descriptor(
  name='ExportAgentResponse',
  full_name='google.cloud.dialogflow.v2.ExportAgentResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agent_uri', full_name='google.cloud.dialogflow.v2.ExportAgentResponse.agent_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_content', full_name='google.cloud.dialogflow.v2.ExportAgentResponse.agent_content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='agent', full_name='google.cloud.dialogflow.v2.ExportAgentResponse.agent',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=927,
  serialized_end=1003,
)


_IMPORTAGENTREQUEST = _descriptor.Descriptor(
  name='ImportAgentRequest',
  full_name='google.cloud.dialogflow.v2.ImportAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.ImportAgentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_uri', full_name='google.cloud.dialogflow.v2.ImportAgentRequest.agent_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_content', full_name='google.cloud.dialogflow.v2.ImportAgentRequest.agent_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='agent', full_name='google.cloud.dialogflow.v2.ImportAgentRequest.agent',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1005,
  serialized_end=1096,
)


_RESTOREAGENTREQUEST = _descriptor.Descriptor(
  name='RestoreAgentRequest',
  full_name='google.cloud.dialogflow.v2.RestoreAgentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.RestoreAgentRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_uri', full_name='google.cloud.dialogflow.v2.RestoreAgentRequest.agent_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agent_content', full_name='google.cloud.dialogflow.v2.RestoreAgentRequest.agent_content', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='agent', full_name='google.cloud.dialogflow.v2.RestoreAgentRequest.agent',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1098,
  serialized_end=1190,
)

_AGENT.fields_by_name['match_mode'].enum_type = _AGENT_MATCHMODE
_AGENT_MATCHMODE.containing_type = _AGENT
_SEARCHAGENTSRESPONSE.fields_by_name['agents'].message_type = _AGENT
_EXPORTAGENTRESPONSE.oneofs_by_name['agent'].fields.append(
  _EXPORTAGENTRESPONSE.fields_by_name['agent_uri'])
_EXPORTAGENTRESPONSE.fields_by_name['agent_uri'].containing_oneof = _EXPORTAGENTRESPONSE.oneofs_by_name['agent']
_EXPORTAGENTRESPONSE.oneofs_by_name['agent'].fields.append(
  _EXPORTAGENTRESPONSE.fields_by_name['agent_content'])
_EXPORTAGENTRESPONSE.fields_by_name['agent_content'].containing_oneof = _EXPORTAGENTRESPONSE.oneofs_by_name['agent']
_IMPORTAGENTREQUEST.oneofs_by_name['agent'].fields.append(
  _IMPORTAGENTREQUEST.fields_by_name['agent_uri'])
_IMPORTAGENTREQUEST.fields_by_name['agent_uri'].containing_oneof = _IMPORTAGENTREQUEST.oneofs_by_name['agent']
_IMPORTAGENTREQUEST.oneofs_by_name['agent'].fields.append(
  _IMPORTAGENTREQUEST.fields_by_name['agent_content'])
_IMPORTAGENTREQUEST.fields_by_name['agent_content'].containing_oneof = _IMPORTAGENTREQUEST.oneofs_by_name['agent']
_RESTOREAGENTREQUEST.oneofs_by_name['agent'].fields.append(
  _RESTOREAGENTREQUEST.fields_by_name['agent_uri'])
_RESTOREAGENTREQUEST.fields_by_name['agent_uri'].containing_oneof = _RESTOREAGENTREQUEST.oneofs_by_name['agent']
_RESTOREAGENTREQUEST.oneofs_by_name['agent'].fields.append(
  _RESTOREAGENTREQUEST.fields_by_name['agent_content'])
_RESTOREAGENTREQUEST.fields_by_name['agent_content'].containing_oneof = _RESTOREAGENTREQUEST.oneofs_by_name['agent']
DESCRIPTOR.message_types_by_name['Agent'] = _AGENT
DESCRIPTOR.message_types_by_name['GetAgentRequest'] = _GETAGENTREQUEST
DESCRIPTOR.message_types_by_name['SearchAgentsRequest'] = _SEARCHAGENTSREQUEST
DESCRIPTOR.message_types_by_name['SearchAgentsResponse'] = _SEARCHAGENTSRESPONSE
DESCRIPTOR.message_types_by_name['TrainAgentRequest'] = _TRAINAGENTREQUEST
DESCRIPTOR.message_types_by_name['ExportAgentRequest'] = _EXPORTAGENTREQUEST
DESCRIPTOR.message_types_by_name['ExportAgentResponse'] = _EXPORTAGENTRESPONSE
DESCRIPTOR.message_types_by_name['ImportAgentRequest'] = _IMPORTAGENTREQUEST
DESCRIPTOR.message_types_by_name['RestoreAgentRequest'] = _RESTOREAGENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Agent = _reflection.GeneratedProtocolMessageType('Agent', (_message.Message,), dict(
  DESCRIPTOR = _AGENT,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """Represents a conversational agent.
  
  
  Attributes:
      parent:
          Required. The project of this agent. Format:
          ``projects/<Project ID>``.
      display_name:
          Required. The name of this agent.
      default_language_code:
          Required. The default language of the agent as a language tag.
          See `Language Support
          <https://dialogflow.com/docs/reference/language>`__ for a list
          of the currently supported language codes. This field cannot
          be set by the ``Update`` method.
      supported_language_codes:
          Optional. The list of all languages supported by this agent
          (except for the ``default_language_code``).
      time_zone:
          Required. The time zone of this agent from the `time zone
          database <https://www.iana.org/time-zones>`__, e.g.,
          America/New\_York, Europe/Paris.
      description:
          Optional. The description of this agent. The maximum length is
          500 characters. If exceeded, the request is rejected.
      avatar_uri:
          Optional. The URI of the agent's avatar. Avatars are used
          throughout the Dialogflow console and in the self-hosted `Web
          Demo <https://dialogflow.com/docs/integrations/web-demo>`__
          integration.
      enable_logging:
          Optional. Determines whether this agent should log
          conversation queries.
      match_mode:
          Optional. Determines how intents are detected from user
          queries.
      classification_threshold:
          Optional. To filter out false positive results and still get
          variety in matched natural language inputs for your agent, you
          can tune the machine learning classification threshold. If the
          returned score value is less than the threshold value, then a
          fallback intent is be triggered or, if there are no fallback
          intents defined, no intent will be triggered. The score values
          range from 0.0 (completely uncertain) to 1.0 (completely
          certain). If set to 0.0, the default of 0.3 is used.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.Agent)
  ))
_sym_db.RegisterMessage(Agent)

GetAgentRequest = _reflection.GeneratedProtocolMessageType('GetAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETAGENTREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.GetAgent][google.cloud.dialogflow.v2.Agents.GetAgent].
  
  
  Attributes:
      parent:
          Required. The project that the agent to fetch is associated
          with. Format: ``projects/<Project ID>``.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.GetAgentRequest)
  ))
_sym_db.RegisterMessage(GetAgentRequest)

SearchAgentsRequest = _reflection.GeneratedProtocolMessageType('SearchAgentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAGENTSREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.SearchAgents][google.cloud.dialogflow.v2.Agents.SearchAgents].
  
  
  Attributes:
      parent:
          Required. The project to list agents from. Format:
          ``projects/<Project ID or '-'>``.
      page_size:
          Optional. The maximum number of items to return in a single
          page. By default 100 and at most 1000.
      page_token:
          Optional. The next\_page\_token value returned from a previous
          list request.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.SearchAgentsRequest)
  ))
_sym_db.RegisterMessage(SearchAgentsRequest)

SearchAgentsResponse = _reflection.GeneratedProtocolMessageType('SearchAgentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SEARCHAGENTSRESPONSE,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The response message for
  [Agents.SearchAgents][google.cloud.dialogflow.v2.Agents.SearchAgents].
  
  
  Attributes:
      agents:
          The list of agents. There will be a maximum number of items
          returned based on the page\_size field in the request.
      next_page_token:
          Token to retrieve the next page of results, or empty if there
          are no more results in the list.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.SearchAgentsResponse)
  ))
_sym_db.RegisterMessage(SearchAgentsResponse)

TrainAgentRequest = _reflection.GeneratedProtocolMessageType('TrainAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRAINAGENTREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.TrainAgent][google.cloud.dialogflow.v2.Agents.TrainAgent].
  
  
  Attributes:
      parent:
          Required. The project that the agent to train is associated
          with. Format: ``projects/<Project ID>``.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.TrainAgentRequest)
  ))
_sym_db.RegisterMessage(TrainAgentRequest)

ExportAgentRequest = _reflection.GeneratedProtocolMessageType('ExportAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTAGENTREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent].
  
  
  Attributes:
      parent:
          Required. The project that the agent to export is associated
          with. Format: ``projects/<Project ID>``.
      agent_uri:
          Optional. The Google Cloud Storage URI to export the agent to.
          Note: The URI must start with "gs://". If left unspecified,
          the serialized agent is returned inline.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ExportAgentRequest)
  ))
_sym_db.RegisterMessage(ExportAgentRequest)

ExportAgentResponse = _reflection.GeneratedProtocolMessageType('ExportAgentResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXPORTAGENTRESPONSE,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The response message for
  [Agents.ExportAgent][google.cloud.dialogflow.v2.Agents.ExportAgent].
  
  
  Attributes:
      agent:
          Required. The exported agent.
      agent_uri:
          The URI to a file containing the exported agent. This field is
          populated only if ``agent_uri`` is specified in
          ``ExportAgentRequest``.
      agent_content:
          The exported agent.  Example for how to export an agent to a
          zip file via a command line:  | curl |
          'https://dialogflow.googleapis.com/v2/projects//agent:export'
          | -X POST | -H 'Authorization: Bearer '$(gcloud auth print-
          access-token) | -H 'Accept: application/json' | -H 'Content-
          Type: application/json' | --compressed | --data-binary '{}' |
          \| grep agentContent \| sed -e 's/.*"agentContent":
          "([^"]*)".\*/:raw-latex:`\1`/' | \| base64 --decode >
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ExportAgentResponse)
  ))
_sym_db.RegisterMessage(ExportAgentResponse)

ImportAgentRequest = _reflection.GeneratedProtocolMessageType('ImportAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _IMPORTAGENTREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.ImportAgent][google.cloud.dialogflow.v2.Agents.ImportAgent].
  
  
  Attributes:
      parent:
          Required. The project that the agent to import is associated
          with. Format: ``projects/<Project ID>``.
      agent:
          Required. The agent to import.
      agent_uri:
          The URI to a Google Cloud Storage file containing the agent to
          import. Note: The URI must start with "gs://".
      agent_content:
          The agent to import.  Example for how to import an agent via
          the command line:  | curl |
          'https://dialogflow.googleapis.com/v2/projects//agent:import |
          -X POST | -H 'Authorization: Bearer ':math:`(gcloud auth
          print-access-token) \    -H 'Accept: application/json' \    -H
          'Content-Type: application/json' \    --compressed \
          --data-binary "{  'agentContent': '`\ (cat \| base64 -w 0)' }"
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ImportAgentRequest)
  ))
_sym_db.RegisterMessage(ImportAgentRequest)

RestoreAgentRequest = _reflection.GeneratedProtocolMessageType('RestoreAgentRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESTOREAGENTREQUEST,
  __module__ = 'google.cloud.dialogflow_v2.proto.agent_pb2'
  ,
  __doc__ = """The request message for
  [Agents.RestoreAgent][google.cloud.dialogflow.v2.Agents.RestoreAgent].
  
  
  Attributes:
      parent:
          Required. The project that the agent to restore is associated
          with. Format: ``projects/<Project ID>``.
      agent:
          Required. The agent to restore.
      agent_uri:
          The URI to a Google Cloud Storage file containing the agent to
          restore. Note: The URI must start with "gs://".
      agent_content:
          The agent to restore.  Example for how to restore an agent via
          the command line:  | curl |
          'https://dialogflow.googleapis.com/v2/projects//agent:restore
          | -X POST | -H 'Authorization: Bearer ':math:`(gcloud auth
          print-access-token) \    -H 'Accept: application/json' \    -H
          'Content-Type: application/json' \    --compressed \
          --data-binary "{  'agentContent': '`\ (cat \| base64 -w 0)' }"
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.RestoreAgentRequest)
  ))
_sym_db.RegisterMessage(RestoreAgentRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\036com.google.cloud.dialogflow.v2B\nAgentProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2'))

_AGENTS = _descriptor.ServiceDescriptor(
  name='Agents',
  full_name='google.cloud.dialogflow.v2.Agents',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1193,
  serialized_end=2071,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAgent',
    full_name='google.cloud.dialogflow.v2.Agents.GetAgent',
    index=0,
    containing_service=None,
    input_type=_GETAGENTREQUEST,
    output_type=_AGENT,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\037\022\035/v2/{parent=projects/*}/agent')),
  ),
  _descriptor.MethodDescriptor(
    name='SearchAgents',
    full_name='google.cloud.dialogflow.v2.Agents.SearchAgents',
    index=1,
    containing_service=None,
    input_type=_SEARCHAGENTSREQUEST,
    output_type=_SEARCHAGENTSRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002&\022$/v2/{parent=projects/*}/agent:search')),
  ),
  _descriptor.MethodDescriptor(
    name='TrainAgent',
    full_name='google.cloud.dialogflow.v2.Agents.TrainAgent',
    index=2,
    containing_service=None,
    input_type=_TRAINAGENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002(\"#/v2/{parent=projects/*}/agent:train:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='ExportAgent',
    full_name='google.cloud.dialogflow.v2.Agents.ExportAgent',
    index=3,
    containing_service=None,
    input_type=_EXPORTAGENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v2/{parent=projects/*}/agent:export:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='ImportAgent',
    full_name='google.cloud.dialogflow.v2.Agents.ImportAgent',
    index=4,
    containing_service=None,
    input_type=_IMPORTAGENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v2/{parent=projects/*}/agent:import:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='RestoreAgent',
    full_name='google.cloud.dialogflow.v2.Agents.RestoreAgent',
    index=5,
    containing_service=None,
    input_type=_RESTOREAGENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002*\"%/v2/{parent=projects/*}/agent:restore:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENTS)

DESCRIPTOR.services_by_name['Agents'] = _AGENTS

# @@protoc_insertion_point(module_scope)
