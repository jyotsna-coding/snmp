"""
This simulates a SNMP device which sends information through UDP port 162
"""
import sys, os
import socket
from time import sleep
import logging

if __name__ == '__main__':
    sys.path.insert(0, '../../')

from Snmp_practice.load_yaml import conf
from Snmp_practice import logger

log = logger.Logger('snmp_dev')
# logging.basicConfig(filename=conf['log_file'],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
    if conf is None:

        log.app_log.error("Config yaml error return None")
        sys.exit()

except Exception as e:

        log.app_log.error(e)

UDP_IP = conf['UDP_IP']
UDP_PORT = conf['UDP_PORT']
MESSAGE = "SNMP SNMP SNMP"

clt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        clt.sendto(bytes(MESSAGE,"utf-8"),(UDP_IP,UDP_PORT))
        log.app_log.info("message sent is: '%s'" % MESSAGE)
        sleep(10)
    except KeyboardInterrupt:
        clt.sendto(bytes("quit","utf-8"),(UDP_IP,UDP_PORT))
        clt.close()
        exit()
