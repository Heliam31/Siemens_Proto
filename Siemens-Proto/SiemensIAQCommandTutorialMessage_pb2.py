# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SiemensIAQCommandTutorialMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&SiemensIAQCommandTutorialMessage.proto\x1a\x0cnanopb.proto\"\xf5\x03\n SiemensIAQCommandTutorialMessage\x12\x46\n\x04mode\x18\x01 \x02(\x0e\x32\x38.SiemensIAQCommandTutorialMessage.SiemensIAQTutorialMode\"\x88\x03\n\x16SiemensIAQTutorialMode\x12\x19\n\x15SIEMENS_TUTORIAL_TEMP\x10\x00\x12\x1a\n\x16SIEMENS_TUTORIAL_HUMID\x10\x01\x12\x18\n\x14SIEMENS_TUTORIAL_CO2\x10\x02\x12\x18\n\x14SIEMENS_TUTORIAL_VOC\x10\x03\x12\x19\n\x15SIEMENS_TUTORIAL_DUST\x10\x04\x12 \n\x1cSIEMENS_TUTORIAL_WHITE_BLINK\x10\x05\x12 \n\x1cSIEMENS_TUTORIAL_WHITE_SOLID\x10\x06\x12\x19\n\x15SIEMENS_TUTORIAL_GOOD\x10\x07\x12\x19\n\x15SIEMENS_TUTORIAL_FAIR\x10\x08\x12\x19\n\x15SIEMENS_TUTORIAL_POOR\x10\t\x12\x1a\n\x16SIEMENS_TUTORIAL_SCORE\x10\n\x12\x19\n\x15SIEMENS_TUTORIAL_EXIT\x10\x0b\x12\x1c\n\x18SIEMENS_TUTORIAL_UNKNOWN\x10\x0c')



_SIEMENSIAQCOMMANDTUTORIALMESSAGE = DESCRIPTOR.message_types_by_name['SiemensIAQCommandTutorialMessage']
_SIEMENSIAQCOMMANDTUTORIALMESSAGE_SIEMENSIAQTUTORIALMODE = _SIEMENSIAQCOMMANDTUTORIALMESSAGE.enum_types_by_name['SiemensIAQTutorialMode']
SiemensIAQCommandTutorialMessage = _reflection.GeneratedProtocolMessageType('SiemensIAQCommandTutorialMessage', (_message.Message,), {
  'DESCRIPTOR' : _SIEMENSIAQCOMMANDTUTORIALMESSAGE,
  '__module__' : 'SiemensIAQCommandTutorialMessage_pb2'
  # @@protoc_insertion_point(class_scope:SiemensIAQCommandTutorialMessage)
  })
_sym_db.RegisterMessage(SiemensIAQCommandTutorialMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SIEMENSIAQCOMMANDTUTORIALMESSAGE._serialized_start=57
  _SIEMENSIAQCOMMANDTUTORIALMESSAGE._serialized_end=558
  _SIEMENSIAQCOMMANDTUTORIALMESSAGE_SIEMENSIAQTUTORIALMODE._serialized_start=166
  _SIEMENSIAQCOMMANDTUTORIALMESSAGE_SIEMENSIAQTUTORIALMODE._serialized_end=558
# @@protoc_insertion_point(module_scope)
