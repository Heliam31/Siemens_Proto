# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SiemensIAQEventSysInfoMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#SiemensIAQEventSysInfoMessage.proto\x1a\x0cnanopb.proto\"\x87\x02\n\x1dSiemensIAQEventSysInfoMessage\x12\x0e\n\x06reason\x18\x01 \x02(\t\x12\x18\n\x10\x66irmware_version\x18\x02 \x02(\t\x12\x13\n\x0bmac_address\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\r\x12\x13\n\x04rssi\x18\x05 \x02(\x05\x42\x05\x92?\x02\x38\x10\x12\x14\n\x0cutc_time_sec\x18\x06 \x01(\r\x12$\n\x15utc_offset_in_minutes\x18\x07 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12$\n\x15\x64st_offset_in_minutes\x18\x08 \x01(\x05\x42\x05\x92?\x02\x38\x10\x12\x0e\n\x06\x64st_on\x18\t \x01(\t\x12\x0f\n\x07\x64st_off\x18\n \x01(\t')



_SIEMENSIAQEVENTSYSINFOMESSAGE = DESCRIPTOR.message_types_by_name['SiemensIAQEventSysInfoMessage']
SiemensIAQEventSysInfoMessage = _reflection.GeneratedProtocolMessageType('SiemensIAQEventSysInfoMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIEMENSIAQEVENTSYSINFOMESSAGE,
  '__module__' : 'SiemensIAQEventSysInfoMessage_pb2'
  # @@protoc_insertion_point(class_scope:SiemensIAQEventSysInfoMessage)
  })
_sym_db.RegisterMessage(SiemensIAQEventSysInfoMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['rssi']._options = None
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['rssi']._serialized_options = b'\222?\0028\020'
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['utc_offset_in_minutes']._options = None
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['utc_offset_in_minutes']._serialized_options = b'\222?\0028\020'
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['dst_offset_in_minutes']._options = None
  _SIEMENSIAQEVENTSYSINFOMESSAGE.fields_by_name['dst_offset_in_minutes']._serialized_options = b'\222?\0028\020'
  _SIEMENSIAQEVENTSYSINFOMESSAGE._serialized_start=54
  _SIEMENSIAQEVENTSYSINFOMESSAGE._serialized_end=317
# @@protoc_insertion_point(module_scope)
