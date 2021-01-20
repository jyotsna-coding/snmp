"""
This receives from snmp device the data on udp port 162
and sends to server on tcp port 8768
"""
import sys, os
import socket
from time import sleep

import logging

if __name__ == '__main__':
    sys.path.insert(0, '../')

from load_yaml import conf

log = logging.getLogger('slave')
logging.basicConfig(filename=conf['log_file'], level=logging.INFO)

try:
    if conf is None:

        log.error("Config yaml error return None")
        sys.exit()
except Exception as e:

        log.error(e)

UDP_IP = conf['UDP_IP']
UDP_PORT = conf['UDP_PORT']

TCP_IP = conf['TCP_IP']
TCP_PORT = conf['TCP_PORT']

clt_tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clt_tcpsock.connect((TCP_IP, TCP_PORT))

serv_udpsock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serv_udpsock.bind((UDP_IP,UDP_PORT))

while True:
    try:
        data,addr = serv_udpsock.recvfrom(1024)
        if (data == b"quit"):
            clt_tcpsock.send(data)
            serv_udpsock.close()
            clt_tcpsock.close()
            exit()
        if (data == b"") or (b'empty' in data):
            continue
        log.info("Received message: %s " %data)

        clt_tcpsock.send(data)

    except KeyboardInterrupt:
        serv_udpsock.close()
        clt_tcpsock.close()
        exit()




