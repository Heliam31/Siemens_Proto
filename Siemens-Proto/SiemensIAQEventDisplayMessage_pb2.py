# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SiemensIAQEventDisplayMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#SiemensIAQEventDisplayMessage.proto\x1a\x0cnanopb.proto\"\xbd\x05\n\x1dSiemensIAQEventDisplayMessage\x12\x42\n\x04mode\x18\x01 \x02(\x0e\x32\x34.SiemensIAQEventDisplayMessage.SiemensIAQDisplayMode\x12\x19\n\nbrightness\x18\x02 \x02(\rB\x05\x92?\x02\x38\x08\"\xbc\x04\n\x15SiemensIAQDisplayMode\x12\x18\n\x14SIEMENS_DISP_DEFAULT\x10\x00\x12\x16\n\x12SIEMENS_DISP_SCORE\x10\x01\x12\x16\n\x12SIEMENS_DISP_CLOCK\x10\x02\x12\x1b\n\x17SIEMENS_DISP_CLOCK_24HR\x10\x03\x12\x1b\n\x17SIEMENS_DISP_TEMP_HUMID\x10\x04\x12\x1d\n\x19SIEMENS_DISP_TEMP_HUMID_C\x10\x05\x12\x1d\n\x19SIEMENS_DISP_TEMP_HUMID_F\x10\x06\x12\x15\n\x11SIEMENS_DISP_TEMP\x10\x07\x12\x17\n\x13SIEMENS_DISP_TEMP_C\x10\x08\x12\x17\n\x13SIEMENS_DISP_TEMP_F\x10\t\x12\x16\n\x12SIEMENS_DISP_HUMID\x10\n\x12\x14\n\x10SIEMENS_DISP_CO2\x10\x0b\x12\x14\n\x10SIEMENS_DISP_VOC\x10\x0c\x12\x15\n\x11SIEMENS_DISP_DUST\x10\r\x12\x1d\n\x19SIEMENS_DISP_DUST_PM2DOT5\x10\x0e\x12\x1a\n\x16SIEMENS_DISP_DUST_PM10\x10\x0f\x12\x18\n\x14SIEMENS_DISP_BATTERY\x10\x10\x12\x1a\n\x16SIEMENS_DISP_DEVICE_ID\x10\x11\x12\x15\n\x11SIEMENS_DISP_TEXT\x10\x12\x12\x1b\n\x17SIEMENS_DISP_TOGGLE_ALL\x10\x13\x12\x18\n\x14SIEMENS_DISP_UNKNOWN\x10\x14')



_SIEMENSIAQEVENTDISPLAYMESSAGE = DESCRIPTOR.message_types_by_name['SiemensIAQEventDisplayMessage']
_SIEMENSIAQEVENTDISPLAYMESSAGE_SIEMENSIAQDISPLAYMODE = _SIEMENSIAQEVENTDISPLAYMESSAGE.enum_types_by_name['SiemensIAQDisplayMode']
SiemensIAQEventDisplayMessage = _reflection.GeneratedProtocolMessageType('SiemensIAQEventDisplayMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIEMENSIAQEVENTDISPLAYMESSAGE,
  '__module__' : 'SiemensIAQEventDisplayMessage_pb2'
  # @@protoc_insertion_point(class_scope:SiemensIAQEventDisplayMessage)
  })
_sym_db.RegisterMessage(SiemensIAQEventDisplayMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIEMENSIAQEVENTDISPLAYMESSAGE.fields_by_name['brightness']._options = None
  _SIEMENSIAQEVENTDISPLAYMESSAGE.fields_by_name['brightness']._serialized_options = b'\222?\0028\010'
  _SIEMENSIAQEVENTDISPLAYMESSAGE._serialized_start=54
  _SIEMENSIAQEVENTDISPLAYMESSAGE._serialized_end=755
  _SIEMENSIAQEVENTDISPLAYMESSAGE_SIEMENSIAQDISPLAYMODE._serialized_start=183
  _SIEMENSIAQEVENTDISPLAYMESSAGE_SIEMENSIAQDISPLAYMODE._serialized_end=755
# @@protoc_insertion_point(module_scope)
