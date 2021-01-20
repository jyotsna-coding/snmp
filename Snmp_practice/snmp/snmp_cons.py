"""
This is a Kafka Consumer basic code to receive data from
Kafka Producer
"""
import os, sys
import logging

if __name__ == '__main__':
    sys.path.insert(0, '../../')

from Snmp_practice.load_yaml import conf
from Snmp_practice import logger

log = logger.Logger('snmp_cons')
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

from kafka import KafkaConsumer

consumer = KafkaConsumer('first_topic',
                         bootstrap_servers=[conf['k_host_port']])
try:
    for message in consumer:
        if message.value == b"quit":
            log.app_log.info("Message Transfer Completed")
            exit()
        log.app_log.info(message)
except KeyboardInterrupt:
    exit()

