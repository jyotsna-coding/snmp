import logging
import sys
import os
from .load_yaml import conf
from logging.handlers import RotatingFileHandler

try:
    if conf is None:
        sys.exit('conf is none in logger')
except Exception as e:
    sys.exit(e)


class Logger:

    def __init__(self, name):
        try:
            # log_dir = conf['log_dir']

            self.app_log = logging.getLogger(name)
            self.app_log.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            logFile = conf['log_file']
            logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=int(conf['log_rotate_length']),
                                         backupCount=int(conf['log_max_rotated_files']), encoding=None)
            logHandler.setLevel(logging.INFO)
            logHandler.setFormatter(formatter)

            # errlogFile = str(log_dir) + str(errfilename) + '.txt'
            # errorLogHandler = RotatingFileHandler(errlogFile, mode='a', maxBytes=int(conf['log_rotate_length']),
            #                                   backupCount=int(conf['log_max_rotated_files']), encoding=None)
            # errorLogHandler.setLevel(logging.ERROR)
            # errorLogHandler.setFormatter(formatter)

            self.app_log.addHandler(logHandler)
            # self.app_log.addHandler(errorLogHandler)

        except Exception as e:
            self.app_log.error(error_text=e)

    def get_Logger(self):
        return self.app_log
