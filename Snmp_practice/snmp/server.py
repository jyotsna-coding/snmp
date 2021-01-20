"""
This server reveives the snmp trap data through TCP port
8768 to be sent to Kafka Server
"""
import socket
import os, sys
from time import sleep
from kafka import KafkaProducer

import logging

if __name__ == '__main__':
    sys.path.insert(0, '../../')

from Snmp_practice.load_yaml import conf
from Snmp_practice import logger

log = logger.Logger('server')
# logging.basicConfig(filename=conf['log_file'],format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

try:
    if conf is None:

        log.app_log.error("Config yaml error return None")
        sys.exit()

except Exception as e:

    print(
        'Error on line :', str(sys.exc_info()[-1].tb_lineno),
        ' Error Type:', str(type(e).__name__),
        ' Error Desc:', str(e),
        ' File Name:', str(os.path.basename(
            sys.exc_info()[2].tb_frame.f_code.co_filename
            )))

producer = KafkaProducer(bootstrap_servers =[conf['k_host_port']])

TCP_IP = conf['TCP_IP']
TCP_PORT = conf['TCP_PORT']

serv_tcpsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_tcpsock.bind((TCP_IP,TCP_PORT))
serv_tcpsock.listen(5)
conn,addr = serv_tcpsock.accept()
while True:
    try:
        data = conn.recv(1024)
        if (data == b"") or (b'empty' in data):
            continue
        log.app_log.info(data)

        producer.send('first_topic',data)
        producer.flush()
        if (data == b"quit"):
            serv_tcpsock.close()
            exit()
    except KeyboardInterrupt:
        serv_tcpsock.close()
        exit()


