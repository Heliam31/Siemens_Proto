"""
 -*- coding: utf-8 -*-

 sensOCampus configuration module.
   Will retrieve both informations:
   - MQTT credentials
   - node configuration (i.e topic ans specific module setup)

 M.Poitelea    mar.24   modifications for Modbus PIABTP POC
 F.Thiebolt    may.23   add support for 'test' mode
 Thiebolt F.   Oct.17   take parameters 'server' and 'port' from credentials
 T.Bueno       May.16   initial commit

 
"""
#!/usr/bin/env python3

# #############################################################################
#
# Import zone
#

import json
import os.path
import time
import logging
import subprocess
import socket
import fcntl
import struct

import requests

# #############################################################################
#
# Configuration of our logging
#

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    handlers=[
        logging.FileHandler("/tmp/modbus.log"),
        logging.StreamHandler()
    ]
    )

# #############################################################################
#
# Class
#
class Configuration(object):
    """ Class importing our config and saving our credentials"""
    initialized = None
    login = None
    password = None
    broker_adress = None
    port = None
    topic = None
    baudrate = None
    timeout = None
    portname = None

    _test = True

    def __init__(self):

        self.initialized = False
        logging.debug("configuration initialization started")

        # try to load the configuration file
        # (at least to retrieve the password if any)
        self.load()

        while not self.initialized:
            # Using Test Mode? 
            if self._test is True:
                logging.info("[TEST] TEST MODE ACTIVATED ... will substitute credentials/topics ...")
                self.login = "test"
                self.password = "test"
                self.topic = "TestTopic/PIABTP/POCMRL/Modbus"
                self.baudrate = 9600
                self.timeout = 0.3
                self.portname = "/dev/ttyUSB0"
                self.broker_adress = self.broker_adress if self.broker_adress is not None else "autocampus.fr"
                self.port = self.port if self.port is not None else 10883
                self.initialized = True
                break
            # retrieve CREDENTIALS from HTTP(S) and create config file

            if not self.http_get_credentials() or not self.load() :
                logging.debug("failed to retrieve CREDENTIALS ... reset ... sleeping 10s ...")
                self.reset()
                time.sleep(10)
                continue

            # connect to senOCampus and retrieve CONFIG from HTTP(S)
            if self.update() is not True:
                logging.error("failed to retrieve CONFIG from sensOCampus ... reset CREDENTIALS and restart ...")
                self.reset()
                time.sleep(10)
            else:
                logging.info("device's CONFIG successfully loaded, device is initialized :)")

        # success :)

    def load(self):
        ''' Load CREDENTIALS from credentials file '''
        if self.initialized:
            logging.debug("configuration already initialized, stopping")
            return True

        if not self.exists():
            logging.info("either config file does not exists or is invalid")
            return False

        try:
            json_file = open("credentials.json",'r', encoding="utf-8")
        except FileNotFoundError:
            logging.info("file was not imported")
            return False

        json_data = json.load(json_file)
        json_file.close()

        self.broker_adress = json_data[0]['addr']
        self.port = json_data[0]['port']
        self.user = json_data[0]['login']
        self.passw = json_data[0]['pass']
        self.topic = json_data[0]['topic']

        return True

    def exists(self):
        ''' Check if a valid CONFIG FILE containing CREDENTIALS exists ... '''
        logging.debug("checking for existing credentials")

        try:
            json_file = open("credentials.json",'r', encoding="utf-8")
        except FileNotFoundError:
            logging.info("file doesn't exist")
            return False

        rd = json.load(json_file)
        rd = rd[0]
        json_file.close()

        if "topic" not in rd:
            logging.debug("credentials file exists, but topic not here")
            return False

        if "addr" not in rd:
            logging.debug("credentials file exists, but addr not here")
            return False

        if 'port' not in rd:
            logging.debug("credentials file exists, but port not here")

        # minimum required in saved credentials are 'login' and 'password'
        if 'login' not in rd:
            logging.debug("credentials file exists, but is missing login field")
            return False

        if 'pass' not in rd:
            logging.debug("credentials file exists, but is missing password field")
            return False

        logging.debug("credentials file exists and is valid")
        return True

    def reset(self):
        ''' reset all credentials and DELETE configuration file '''
        self._login = None
        self._password = None
        self._server = None
        self._port = None
        self._topics = None
        self._initialized = False
        self.baudrate = None
        self.timeout = None
        self.portname = None

        try:
            os.remove("credentials.json")
        except Exception as ex:
            e = str(ex)
            logging.debug("exception while removing CONFIG_FILE: %s", e )


    def getip(self,ifname):
        ''' returns IP of an interface '''
        ip = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', bytes(ifname[:15], 'utf-8')))[20:24])
        except OSError:
            return None
        else:
            return ip

    def _get_otp(self):
        """ get OTP rom content"""

        #try:
        #    lines = subprocess.check_output(["vcgencmd","otp_dump"], universal_newlines=True)
        #except (subprocess.CalledProcessError,FileNotFoundError) as ex:
        #    return xxxx

        lines = subprocess.check_output(["vcgencmd","otp_dump"], universal_newlines=True)

        lines = lines.split('\n')

        otp = dict()
        for line in lines[:-1]:
            key, value = line.rstrip("\n").split(':')
            otp[key] = value

        # checks
        if len(otp) < 59 : raise Exception("unusal OTP size '%d' ?!?!" % (len(otp)) )

        return otp


    # def _get_mac(self,func):
    #     ''' Retrieve MAC address from OTP ROM of the Raspberry Pi
    #         Even valid with Pi0!'''
    #     def _wrapper(*args, **kwargs):
    #         _macaddr="00:00:00:00:00:00"
    #         if len(args):
    #             return func(*args, **kwargs)
    #         print("call to low-level _getmac")

    #         try:
    #             otp_dict = self._get_otp()
    #         except Exception as ex:
    #             print("caught exception '%s' while reading OTP rom !" % (str(ex)) )
    #             return _macaddr

    #         # RPi4: mac addr is located key[65] & key[64]
    #         # while <RPi4 3 last digits of mac addr is key[28]
    #         _otpKey = otp_dict.get('65',None)

    #         if _otpKey is None:
    #             print("key 65 does not exists in OTP dict ?!?!")
    #             return _macaddr

    #         if( _otpKey=="00000000" ):
    #             # < RPi4 detected
    #             _submac = otp_dict['28'][2:]
    #             _macaddr="b8:27:eb:" + ':'.join([_submac[i:i+2] for i in range(0,len(_submac),2)])
    #         else:
    #             # Pi4 detected
    #             _submac = otp_dict['65']
    #             _macaddr= ':'.join([_submac[i:i+2] for i in range(0,len(_submac),2)])
    #             _submac = otp_dict['64']
    #             _macaddr += ':'
    #             _macaddr += ':'.join([_submac[i:i+2] for i in range(0,4,2)])
    #         return _macaddr

    #     return _wrapper

    # @_get_mac
    def get_mac(self,interface=None):
        """Return MAC addr of an interface"""
        print("call to high level getmac")
        _ifaceDir = "/sys/class/net/"

        if not interface:
            # select current (active) one
            ifaces = next(os.walk(_ifaceDir))[1]
        else:
            ifaces = [interface, ]

        # Return the MAC address of in-use interface
        for i in ifaces:
            # local interface ?
            if i == "lo":
                continue

            # iface has an IP ?
            try:
                str = open("/sys/class/net/%s/address" % i, "r").readline()
            except Exception:
                str = "00:00:00:00:00:00"

            _ip = self.getip(i)
            if not _ip:
                continue
            print("iface %s[%s] has IP %s" % (i, str[0:17], _ip))
            return str[0:17]

    # def get_mac(self):
    #     """returns MAC adress of our rPi """
    #     mac = "AA:BB:CC:DD:EE:FF"
    #     return mac

    def http_get_credentials(self):
        ''' get credentials from sensOCampus and save them to CONFIG_FILE '''
        #self.reset()
        if self.exists():
            logging.info("credentials already gotten and complete")
            return True

        url = "https://sensocampus.univ-tlse3.fr/device/credentials"
        r = requests.get(url, params={'mac': self.get_mac()}, timeout=10)

        if not r.ok:
            sc = str(r.status_code)
            logging.error("credentials were not delivered by server: status code %s", sc)
            return False

        conf = None
        try:
            conf = json.loads(r.text)
        except Exception as ex:
            e = str(ex)
            logging.error("while validating credentials from server: %s" , e)
            return False

        with open("credentials.json", "w",encoding="utf-8") as f:
            json.dump(conf,f)

        return True

    def update(self):
        ''' try to retrieve CONFIGURATION from sensOCampus '''
        if not self.get_login() or not self.get_password():
            logging.error("tried to grab CONFIG without credentials ?!?!")
            return False

        url = "https://sensocampus.univ-tlse3.fr/device/config"
        r = requests.get(url, auth=(self.get_login(), self.get_password()), timeout=10)

        if not r.ok:
            sc = str(r.status_code)
            logging.error("config was not delivered by server: status code %s" , sc)
            return False

        conf = None
        try:
            conf = json.loads(r.text)
        except Exception as ex:
            e = str(ex)
            logging.error("while validating config from server: %s" , e )
            return False

        for module in conf[0]['modules']:
            if module['module'] == "SensorsPIABTP" and module['unit'] == "modbus_rs485":

                #We found the right module
                for parame in module['params']:
                    #Setting LINK
                    if parame['param'] == "link":
                        self.portname = parame['value']
                        continue
                    #Setting LINK SPEED
                    if parame['param'] == "link_speed":
                        self.baudrate = parame['value']
                        continue
                    #Setting VARIATION_TRESHOLD_CM
                    if parame['param'] == "timeout":
                        self.timeout = parame['value']
                        continue

        # we now have both CREDENTIALS and CONFIG ...
        self._initialized = True

        return self._initialized

    def get_initialized(self):
        """returns if our config files are initialized"""
        return self.initialized

    def get_login(self):
        """returns the login"""
        return self.login

    def get_password(self):
        """returns our password"""
        return self.password

    def get_topic(self):
        """returns our topic"""
        return self.topic

    def get_baudrate(self):
        """return the baudrate"""
        return self.baudrate

    def get_timeout(self):
        """returns the timeout to set for modbus"""
        return self.timeout

    def get_portname(self):
        """return the portname for modbus"""
        return self.portname

    def get_broker_adress(self):
        """returns the adress for the MQTT Broker"""
        return self.broker_adress

    def get_port(self):
        """return the port of the MQTT Broker"""
        return self.port


#
# Execution of import
if __name__ == "__main__":

    kwargs = dict()

    # test mode
    kwargs['test'] = True

    conf = Configuration(**kwargs)
    print(conf.__dict__)
