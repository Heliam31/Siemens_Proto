"""
Scipt used to decode incoming Siemens Protobuf messages
"""

from time import sleep
from datetime import datetime, timedelta
import os
import sys
import csv
import logging
from typing import Any, Optional
import json
import paho.mqtt.client as mqttClient

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

def connect_mqtt (client_id, login, password, addr, port):
    """ Function to connect to the mqtt broker

        Args : client_id(str) used to identify our connection (unique)
               conf(Configuration) : instance of the configuration that contains our credentials
        Returns : client mqtt connected to the broker ready to publish
    """

    client = mqttClient.Client(mqttClient.CallbackAPIVersion.VERSION1,client_id)
    client.username_pw_set(login, password=password)
    client.connect(addr, port=port)

    client.loop_start()        #start the loop

    tries = 3
    sleep(0.2)
    while client.is_connected() is not True and tries > 0:    #Wait for connection
        logging.warning("didnt connect to broker, retrying")
        sleep(1)

    if tries == 0:
        logging.error("Couldn't Connect to the broker")
        return 0

    return client

def subscribe(mqttclient, topic):
    """ Subscribe to mqtt client """
    def on_message(client, userdata, mqttmsg):
        print(f"Received msg from `{mqttmsg.topic}` topic")
        payload = mqttmsg.payload.decode()
        print(payload)
        # msg_dec = msg.SiemensIAQLoraMessage()
        # msg_dec.ParseFromString(bytes.fromhex(payload.data)) #TODO
        # print(msg_dec)
        # if msg_dec.HasField('event_score'):
        #     print("ici sa décode")
        #     tempe = msg_dec.event_score.sensor.temp
        #     humi = msg_dec.event_score.sensor.humid
        #     co2 = msg_dec.event_score.sensor.co2
        #     cov = msg_dec.event_score.sensor.voc
        #     lumi = msg_dec.event_score.sensor.lux

        #     timestamp = "datetime de la trame"#TODO
        #     fourni = "SIEMENS"
        #     sensor_id = fourni + "_" + payload.devEUI[-4:]#TODO
        #     value = json.dumps({"sensorId"  : sensor_id,
        #                     "timestamp" : timestamp,
        #                     "fourni"    : fourni,
        #                     "tempe" : tempe,
        #                     "humi" : humi,
        #                     "co2" : co2,
        #                     "cov" : cov,
        #                     "lumi" : lumi})

        #     if not mqttclient.is_connected():
        #         mqttclient.disconnect()
        #         mqttclient.loop_stop()
        #         mqttclient = connect_mqtt("SiemensNodeRedLora",LOGIN, PASSWORD, ADDR, PORT)
        #         subscribe(mqttclient, topic=topic)
        #         mqttclient.loop_forever()

        #     logging.info("publishing to %s", topic)
        #     mqttclient.publish(topic,value)

    mqttclient.subscribe(topic)
    mqttclient.on_message = on_message

#-------------------------------------------Main----------------------------------------------------

LOGIN = "nodered"
PASSWORD = "test"
ADDR = "neocampus.fr"
PORT = 10882
TOPIC = "_lora/#"
client = connect_mqtt("SiemensNodeRedLora",LOGIN, PASSWORD, ADDR, PORT)

subscribe(client, topic=TOPIC)
client.loop_forever()
