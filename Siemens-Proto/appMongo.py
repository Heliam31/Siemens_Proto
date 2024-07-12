"""
Test Pour faire fonctionner protobuf
"""
import pymongo
import json
import csv
from time import sleep
from datetime import datetime, timedelta
from time import time

#Import protobuf
import SiemensLoRaIAQMessage_pb2 as msg

# ouimec = msgToDec.ParseFromString(bytes.fromhex(rcv))
# print(ouimec)
# print(msgToDec)

def add_csv (addr, time ,measures):
    """write our measures in data.csv
        Args:
            -addr(int)      : adress of our sensor
            -time           : timestamp of the measurement
            -measures(list) : list of our measurements
    """
    fichier = open("data.csv", 'a', newline='', encoding="utf-8")
    cw = csv.writer(fichier)
    cw.writerow([addr] + [time] + measures)
    fichier.close()

#GET MSG FROM MONGODB------------------------------------------------------------------------------------------------------

# client = pymongo.MongoClient("mongodb://apiReader:readerPassword@autocampus.fr:27017/?authMechanism=DEFAULT&authSource=admin")
# # Database Name
# db = client["datalake"]
# # Collection Name
# col = db["_lora"]

# #Get one line
# # x = col.find_one()

# now = datetime.now()
# now_plus_10 = now - timedelta(hours= 5)
# # x = col.find_one({'appargs': "SIEMENS", 'appid' : "PIA-BTP"}, sort ={ "datetime": -1 })
# # print("ouiuiuiuiuohjbjub: ", type(x["datetime"]))
# # x = col.find({'appargs': "SIEMENS", 'appid' : "PIA-BTP", "datetime" : {"$gte" : now_plus_10}}) #, 'datetime':{"$gte":date_newer,"$lt":date_older}
# start = datetime(year=2024, month=3, day=18, hour=14, minute=0, second=0)
# stopaj = datetime(year=2024, month=3, day=27, hour=14, minute=0, second=0)
# cpt_rep = 0
# while start < stopaj:
#     stopped = 0                                                         
#     x = col.find({'appargs': "SIEMENS", 'appid' : "PIA-BTP", "datetime" : {"$gte" : start}} ,limit = 1000 )
#     x = list(x)
#     print(len(x))
#     for line in x:
#         data = line["data"]
#         _id = line["_id"]
#         timestamp = line["datetime"]
#         if timestamp >= stopaj:
#             start = timestamp
#             print("arreted: ",timestamp)
#             stopped = 1
#             break
#         # print("data: ",data)
#         # print("id: ",_id)
#         # print("datetime: ",timestamp, type(timestamp))
#         msgToDec = msg.SiemensIAQLoraMessage()
#         msgToDec.ParseFromString(bytes.fromhex(data))
#         # print(msgToDec)
#         if msgToDec.HasField('event_score'):
#             # print("ici sa décode")
#             print(timestamp)
#             tempe = msgToDec.event_score.sensor.temp
#             humi = msgToDec.event_score.sensor.humid
#             co2 = msgToDec.event_score.sensor.co2
#             cov = msgToDec.event_score.sensor.voc
#             lumi = msgToDec.event_score.sensor.lux
#             sendaj = [_id,tempe,humi,co2,cov,lumi]
#             print(sendaj)
#             sensor_id = "SIEMENS" + line["deveui"][-4:]
#             add_csv(sensor_id, timestamp ,sendaj)
#         if msgToDec.HasField('time_sync_protocol'):
#             if msgToDec.time_sync_protocol.HasField('request'):
#                 add_csv(sensor_id,timestamp,["timesync"])
#         else:
#             if cpt_rep == 100:
#                 add_csv(sensor_id,timestamp,["deviced"])
#                 cpt_rep = 0
#             cpt_rep+=1

#     sleep(0.5)

#     if stopped == 0:
#         last_val = x[-1]
#         start = last_val["datetime"]



#Get msg From .TXT ------------------------------------------------------------------------------------------------------

# #recupération messages
# with open("oui.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()

# #décodage de chaque message
# for line in lines:
#     msgToDec = msg.SiemensIAQLoraMessage()
#     msgToDec.ParseFromString(bytes.fromhex(line))
#     # print(msgToDec)
#     if msgToDec.HasField('event_score'):
#         print("ici sa décode")
#         tempe = msgToDec.event_score.sensor.temp
#         humi = msgToDec.event_score.sensor.humid
#         co2 = msgToDec.event_score.sensor.co2
#         cov = msgToDec.event_score.sensor.voc
#         lumi = msgToDec.event_score.sensor.lux
#         sendaj = [tempe,humi,co2,cov,lumi]
#         print(sendaj)
#     else:
#         print("sa décode pas")

#Get msg From string variable-----------------------------------------------------------------------------------------------------------------------

# rcv = "0A06080210B7960210001A6210001860220A080010001800200028002A210D00FC9E41159442454218AF0420850428E401300338044518BD0A444DC5F7734232290D00FCAE4115EE702E4218AF042085042898033500F411423D003CD1414003480450F32458F280E46E38004000"
# recevaj = "0a06080210b7960210849ae2b206a2011812160a0c4575726f70652f506172697310849ae2b2061800"
# """
# device_uuid {
#   device_type: SIEMENS_OMNI
#   device_id: 35639
# }
# device_timestamp: 0
# time_sync_protocol {
#   response {
#     timezone: "Europe/Paris"
#     utc_in_seconds: 1713449586
#     utc_offset_in_seconds: 0
#   }
# }

# """
# msgToDec = msg.SiemensIAQLoraMessage()
# msgToDec.ParseFromString(bytes.fromhex(recevaj))
# print(msgToDec)
# if msgToDec.HasField('event_score'):
#     print("ici sa décode")
#     tempe = msgToDec.event_score.sensor.temp
#     humi = msgToDec.event_score.sensor.humid
#     co2 = msgToDec.event_score.sensor.co2
#     cov = msgToDec.event_score.sensor.voc
#     lumi = msgToDec.event_score.sensor.lux
#     sendaj = [tempe,humi,co2,cov,lumi]
#     print(sendaj)
# else:
#     print("sa décode pas")

#Encode msg--------------------------------------------------------------------------------------------------------------------------------------------

epoch_time = int(time())
msg_send = msg.SiemensIAQLoraMessage()
msg_send.device_uuid.device_type = "SIEMENS_OMNI"
msg_send.device_uuid.device_id = 35639
msg_send.device_timestamp = epoch_time
msg_send.command_display.mode = 20 #SIEMENS_DISP_TOGGLE_ALL

a = msg_send.SerializeToString()
print(a.hex())

# msg_send.time_sync_protocol.response.timezone = "Europe/Paris"
# msg_send.time_sync_protocol.response.utc_in_seconds = epoch_time
# msg_send.time_sync_protocol.response.utc_offset_in_seconds = 0
