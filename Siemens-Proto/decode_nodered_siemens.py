"""
Script used to decode incoming Siemens Protobuf messages
Mihai POITELEA
"""

import sys
import logging
import json

#Import files
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

#-------------------------------------------Main----------------------------------------------------
trame = sys.argv

for i in trame:
    if i.split(":")[0] == "data":
        data = i.split(":")[1]
    if i.split(":")[0] == "deveui":
        dev_eui = i.split(":")[1]
    if i.split(":")[0] == "datetime":
        timestamp = i.split(":")[1]
    if i.split(":")[0] == "appargs":
        fourni = i.split(":")[1]


msg_dec = msg.SiemensIAQLoraMessage()
msg_dec.ParseFromString(bytes.fromhex(data))

if msg_dec.HasField('event_score'):
    tempe = msg_dec.event_score.sensor.temp
    humi = msg_dec.event_score.sensor.humid
    co2 = msg_dec.event_score.sensor.co2
    cov = msg_dec.event_score.sensor.voc
    lumi = msg_dec.event_score.sensor.lux

    sensor_id = fourni + "_" + dev_eui[-4:]
    value = json.dumps({"payload":{"sensorId"  : sensor_id,
                    "timestamp" : timestamp,
                    "fourni"    : fourni,
                    "tempe" : tempe,
                    "humi" : humi,
                    "co2" : co2,
                    "cov" : cov,
                    "lumi" : lumi}})

    print(value)
