"""
Script used to answer with timestamp to Siemens sensor
Mihai POITELEA
"""

import sys
import logging
from time import time
import SiemensLoRaIAQMessage_pb2 as msg


#------------------------------------------Functions------------------------------------------------

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    handlers=[
        logging.FileHandler("/tmp/modbus.log"),
        logging.StreamHandler()
    ]
    )

def replace_all(txt, old, new):
    for word in old:
        txt = txt.replace(word, new)
    return txt

#-------------------------------------------Main----------------------------------------------------
# trame = sys.argv

# trame_unif = replace_all(trame, ["{", "}", "[" , "]", ","], ":") 

# trame = trame_unif.split(":")

# #print(trame)
# for i in range(len(trame)):
#     if trame[i] == '"data"':
#         data = trame[i+1][1:][:-1]
#         #print("la data est: ",data, " ")
#     if trame[i] == '"deveui"':
#         dev_eui = trame[i+1][1:][:-1]
#         #print("le deveui est: ",dev_eui)
#     if trame[i] == '"datetime"':
#         timestamp = trame[i+3][1:] + ":" + trame[i+4] + ":" + trame[i+5][:-1]
#         #print("la datetime est: ",timestamp)
#     if trame[i] == '"appargs"':
#         fourni = trame[i+1][1:][:-1]
#         #print("la marque est: ",fourni)


msg_dec = msg.SiemensIAQLoraMessage()
# msg_dec.ParseFromString(bytes.fromhex(data))

# msg_dec = msg.SiemensIAQLoraMessage()
msg_dec.ParseFromString(bytes.fromhex("0A06080210B79602100042270A0B6C6F72612D6A6F696E6564120D312E362E322E7369656D656E7328E7FFFFFFFFFFFFFFFF01"))
if msg_dec.HasField("event_sysinfo"):
    msg_send = msg.SiemensIAQLoraMessage()
    msg_send.device_uuid.device_type = "SIEMENS_OMNI"
    msg_send.device_uuid.device_id = 35639
    msg_send.device_timestamp = 0
    msg_send.time_sync_protocol.response.timezone = "Europe/Paris"
    epoch_time = int(time())
    msg_send.time_sync_protocol.response.utc_in_seconds = epoch_time
    msg_send.time_sync_protocol.response.utc_offset_in_seconds = 0

    a = msg_send.SerializeToString()
    print(a)
    print(msg_send)
