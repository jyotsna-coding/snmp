import logging
import sys
import os
from load_yaml import conf
from logging.handlers import RotatingFileHandler

try:
    if conf is None:
        sys.exit('conf is none in logger')
except Exception as e:
    sys.exit(e)


def error_log(log_obj=None, error_text=None):
    if log_obj is None and error_text is not None:

        print(
            'Error on line :' + str(sys.exc_info()[-1].tb_lineno) +
            ' Error Type:' + str(type(error_text).__name__) +
            ' Error Desc:' + str(error_text) +
            ' File Name:' + str(os.path.basename(
                sys.exc_info()[2].tb_frame.f_code.co_filename
            )))

    elif log_obj is not None and error_text is not None:

        log_obj.error(
            'Error on line :' + str(sys.exc_info()[-1].tb_lineno) +
            ' Error Type:' + str(type(error_text).__name__) +
            ' Error Desc:' + str(error_text) +
            ' File Name:' + str(os.path.basename(
                sys.exc_info()[2].tb_frame.f_code.co_filename
            )))


class Logger:

    def __init__(self, filename=None, errfilename=None):
        try:
            log_dir = conf['log_dir']

            self.app_log = logging.getLogger('root')
            self.app_log.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            logFile = str(log_dir) + str(filename) + '.txt'
            logHandler = RotatingFileHandler(logFile, mode='a', maxBytes=int(conf['log_rotate_length']),
                                         backupCount=int(conf['log_max_rotated_files']), encoding=None)
            logHandler.setLevel(logging.INFO)
            logHandler.setFormatter(formatter)

            errlogFile = str(log_dir) + str(errfilename) + '.txt'
            errorLogHandler = RotatingFileHandler(errlogFile, mode='a', maxBytes=int(conf['log_rotate_length']),
                                              backupCount=int(conf['log_max_rotated_files']), encoding=None)
            errorLogHandler.setLevel(logging.ERROR)
            errorLogHandler.setFormatter(formatter)

            self.app_log.addHandler(logHandler)
            self.app_log.addHandler(errorLogHandler)

        except Exception as e:
            error_log(error_text=e)

    def get_Logger(self):
        return self.app_log
