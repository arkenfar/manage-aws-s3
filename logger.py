import os
import logging
import datetime
import glob
from sys import platform

LOG_EXTENTSION = '.log'
LOG_DATE_TIME_FORMAT = '%d%m%Y_%H%M%S'


def path():
    try:
        if operating_system() == "windows":
            file_path = ".\\_log\\"
        else:
            file_path = "./_log/"
        return file_path
    except Exception as err_path:
        raise err_path


def operating_system():
    try:
        if platform == "linux" or platform == "linux2":
            return "linux"
        elif platform == "darwin":
            return "osx"
        elif platform == "win32":
            return "windows"
    except Exception as err_os:
        raise err_os


def clean_up(max_logfiles):
    try:
        counter = 0
        log_path = path()
        files = sorted(glob.glob(log_path + "*" + LOG_EXTENTSION))
        log_msg = f"'{0}' '{1}' file(s) in log path '{2}'".format(
            str(len(files)), LOG_EXTENTSION, log_path)
        logging.info(log_msg)

        if len(files) < max_logfiles:
            log_msg = f"The limit of '{0}' '{1}' files hasn't been reached yet".format(
                str(max_logfiles), LOG_EXTENTSION)
            logging.info(log_msg)
            return
        else:
            log_to_cleanup = len(files) - max_logfiles

        if log_to_cleanup < 1:
            log_msg = "No log files needs to be removed".format(
            )
            logging.info(log_msg)
            return
        else:
            files_to_remove = files[:log_to_cleanup]
            log_msg = f"'{0}' '{1}' file(s) to be removed".format(
                str(len(files_to_remove)), LOG_EXTENTSION)
            logging.info(log_msg)

        for file in files_to_remove:
            try:
                os.remove(file)
                log_msg = f"'{0}' successfully removed".format(
                    LOG_EXTENTSION, file)
                logging.info(log_msg)
                counter += 1
            except Exception as err_cleanup_file:
                err_msg = f"Clean up exception: {0}".format(err_cleanup_file)
                logging.error(err_msg)
                raise err_msg
        log_msg = f"Removed {0} log file(s)".format(str(counter))
        logging.info(log_msg)

    except Exception as err_cleanup:
        raise err_cleanup


def logger(max_logfiles):
    try:
        if not os.path.exists(path()):
            os.makedirs(path())

        logging.basicConfig(filename=path() + datetime.datetime.now().strftime(LOG_DATE_TIME_FORMAT) +
                            LOG_EXTENTSION, level=logging.DEBUG, format='%(asctime)s;%(levelname)s;%(message)s')
        clean_up(max_logfiles)
    except Exception as err_logger:
        logging.error("Logger exception: %s", str(err_logger))
        raise err_logger
