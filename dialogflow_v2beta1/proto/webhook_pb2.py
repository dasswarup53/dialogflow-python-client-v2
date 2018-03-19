# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow_v2beta1/proto/webhook.proto

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
from dialogflow_v2beta1.proto import context_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2
from dialogflow_v2beta1.proto import intent_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2
from dialogflow_v2beta1.proto import session_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow_v2beta1/proto/webhook.proto',
  package='google.cloud.dialogflow.v2beta1',
  syntax='proto3',
  serialized_pb=_b('\n3google/cloud/dialogflow_v2beta1/proto/webhook.proto\x12\x1fgoogle.cloud.dialogflow.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x33google/cloud/dialogflow_v2beta1/proto/context.proto\x1a\x32google/cloud/dialogflow_v2beta1/proto/intent.proto\x1a\x33google/cloud/dialogflow_v2beta1/proto/session.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xe0\x01\n\x0eWebhookRequest\x12\x0f\n\x07session\x18\x04 \x01(\t\x12\x13\n\x0bresponse_id\x18\x01 \x01(\t\x12\x42\n\x0cquery_result\x18\x02 \x01(\x0b\x32,.google.cloud.dialogflow.v2beta1.QueryResult\x12\x64\n\x1eoriginal_detect_intent_request\x18\x03 \x01(\x0b\x32<.google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest\"\xc2\x02\n\x0fWebhookResponse\x12\x18\n\x10\x66ulfillment_text\x18\x01 \x01(\t\x12M\n\x14\x66ulfillment_messages\x18\x02 \x03(\x0b\x32/.google.cloud.dialogflow.v2beta1.Intent.Message\x12\x0e\n\x06source\x18\x03 \x01(\t\x12(\n\x07payload\x18\x04 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x41\n\x0foutput_contexts\x18\x05 \x03(\x0b\x32(.google.cloud.dialogflow.v2beta1.Context\x12I\n\x14\x66ollowup_event_input\x18\x06 \x01(\x0b\x32+.google.cloud.dialogflow.v2beta1.EventInput\"W\n\x1bOriginalDetectIntentRequest\x12\x0e\n\x06source\x18\x01 \x01(\t\x12(\n\x07payload\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructB\xaa\x01\n#com.google.cloud.dialogflow.v2beta1B\x0cWebhookProtoP\x01ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1fGoogle.Cloud.Dialogflow.V2beta1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WEBHOOKREQUEST = _descriptor.Descriptor(
  name='WebhookRequest',
  full_name='google.cloud.dialogflow.v2beta1.WebhookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='google.cloud.dialogflow.v2beta1.WebhookRequest.session', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='response_id', full_name='google.cloud.dialogflow.v2beta1.WebhookRequest.response_id', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_result', full_name='google.cloud.dialogflow.v2beta1.WebhookRequest.query_result', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_detect_intent_request', full_name='google.cloud.dialogflow.v2beta1.WebhookRequest.original_detect_intent_request', index=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=531,
)


_WEBHOOKRESPONSE = _descriptor.Descriptor(
  name='WebhookResponse',
  full_name='google.cloud.dialogflow.v2beta1.WebhookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fulfillment_text', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.fulfillment_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fulfillment_messages', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.fulfillment_messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.payload', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_contexts', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.output_contexts', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='followup_event_input', full_name='google.cloud.dialogflow.v2beta1.WebhookResponse.followup_event_input', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=856,
)


_ORIGINALDETECTINTENTREQUEST = _descriptor.Descriptor(
  name='OriginalDetectIntentRequest',
  full_name='google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest.payload', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=858,
  serialized_end=945,
)

_WEBHOOKREQUEST.fields_by_name['query_result'].message_type = google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2._QUERYRESULT
_WEBHOOKREQUEST.fields_by_name['original_detect_intent_request'].message_type = _ORIGINALDETECTINTENTREQUEST
_WEBHOOKRESPONSE.fields_by_name['fulfillment_messages'].message_type = google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_intent__pb2._INTENT_MESSAGE
_WEBHOOKRESPONSE.fields_by_name['payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_WEBHOOKRESPONSE.fields_by_name['output_contexts'].message_type = google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_context__pb2._CONTEXT
_WEBHOOKRESPONSE.fields_by_name['followup_event_input'].message_type = google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_session__pb2._EVENTINPUT
_ORIGINALDETECTINTENTREQUEST.fields_by_name['payload'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['WebhookRequest'] = _WEBHOOKREQUEST
DESCRIPTOR.message_types_by_name['WebhookResponse'] = _WEBHOOKRESPONSE
DESCRIPTOR.message_types_by_name['OriginalDetectIntentRequest'] = _ORIGINALDETECTINTENTREQUEST

WebhookRequest = _reflection.GeneratedProtocolMessageType('WebhookRequest', (_message.Message,), dict(
  DESCRIPTOR = _WEBHOOKREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.webhook_pb2'
  ,
  __doc__ = """The request message for a webhook call.


  Attributes:
      session:
          The unique identifier of detectIntent request session. Can be
          used to identify end-user inside webhook implementation.
          Format: ``projects/<Project ID>/agent/sessions/<Session ID>``.
      response_id:
          The unique identifier of the response. Contains the same value
          as ``[Streaming]DetectIntentResponse.response_id``.
      query_result:
          The result of the conversational query or event processing.
          Contains the same value as
          ``[Streaming]DetectIntentResponse.query_result``.
      original_detect_intent_request:
          Optional. The contents of the original request that was passed
          to ``[Streaming]DetectIntent`` call.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.WebhookRequest)
  ))
_sym_db.RegisterMessage(WebhookRequest)

WebhookResponse = _reflection.GeneratedProtocolMessageType('WebhookResponse', (_message.Message,), dict(
  DESCRIPTOR = _WEBHOOKRESPONSE,
  __module__ = 'dialogflow_v2beta1.proto.webhook_pb2'
  ,
  __doc__ = """The response message for a webhook call.


  Attributes:
      fulfillment_text:
          Optional. The text to be shown on the screen. This value is
          passed directly to ``QueryResult.fulfillment_text``.
      fulfillment_messages:
          Optional. The collection of rich messages to present to the
          user. This value is passed directly to
          ``QueryResult.fulfillment_messages``.
      source:
          Optional. This value is passed directly to
          ``QueryResult.webhook_source``.
      payload:
          Optional. This value is passed directly to
          ``QueryResult.webhook_payload``.
      output_contexts:
          Optional. The collection of output contexts. This value is
          passed directly to ``QueryResult.output_contexts``.
      followup_event_input:
          Optional. Makes the platform immediately invoke another
          ``DetectIntent`` call internally with the specified event as
          input.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.WebhookResponse)
  ))
_sym_db.RegisterMessage(WebhookResponse)

OriginalDetectIntentRequest = _reflection.GeneratedProtocolMessageType('OriginalDetectIntentRequest', (_message.Message,), dict(
  DESCRIPTOR = _ORIGINALDETECTINTENTREQUEST,
  __module__ = 'dialogflow_v2beta1.proto.webhook_pb2'
  ,
  __doc__ = """Represents the contents of the original request that was passed to the
  ``[Streaming]DetectIntent`` call.


  Attributes:
      source:
          The source of this request, e.g., ``google``, ``facebook``,
          ``slack``. It is set by Dialogflow-owned servers. Possible
          values of this field correspond to [Intent.Message.Platform][g
          oogle.cloud.dialogflow.v2beta1.Intent.Message.Platform].
      payload:
          Optional. This field is set to the value of
          ``QueryParameters.payload`` field passed in the request.
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2beta1.OriginalDetectIntentRequest)
  ))
_sym_db.RegisterMessage(OriginalDetectIntentRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#com.google.cloud.dialogflow.v2beta1B\014WebhookProtoP\001ZIgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2beta1;dialogflow\370\001\001\242\002\002DF\252\002\037Google.Cloud.Dialogflow.V2beta1'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
