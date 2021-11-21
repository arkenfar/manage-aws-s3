import os
import logging
import datetime
import glob
from sys import platform

logFilesExtension = '.log'
logDateTimeFormat = '%d%m%Y_%H%M%S'


def path():
    try:
        if operatinSystem() == "windows":
            fn = ".\\_log\\"
        else:
            fn = "./_log/"
        return fn
    except Exception as E:
        raise


def operatinSystem():
    try:
        if platform == "linux" or platform == "linux2":
            return "linux"
        elif platform == "darwin":
            return "osx"
        elif platform == "win32":
            return "windows"
    except Exception as E:
        raise


def cleanUp(max_logfiles):
    try:
        x = 0
        logPath = path()
        files = sorted(glob.glob(logPath + "*" + logFilesExtension))
        logging.info(str(len(files)) + " " +
                     logFilesExtension + " file(s) in " + logPath)

        if len(files) < max_logfiles:
            logging.info("The limit of " + str(max_logfiles) +
                         " "+logFilesExtension + " files hasn't been reached")
            return
        else:
            y = len(files) - max_logfiles

        if y < 1:
            print("no files needed cleanup")
            return
        else:
            filesToRemove = files[:y]
            print(len(filesToRemove))
            logging.info(str(len(filesToRemove)) +
                         logFilesExtension + " file(s) to be removed")

        for file in filesToRemove:
            try:
                os.remove(file)
                logging.info(logFilesExtension + " '" +
                             file + "' successfully removed")
                x += 1
            except Exception as E:
                logging.error(u'Clean up exception: {0}'.format(str(E)))
                raise
        print("Cleaned up " + str(x) + " log file(s)")
        logging.info("Removed " + str(x) + " log file(s)")

    except Exception as E:
        raise


def logger(max_logfiles):
    try:
        if not os.path.exists(path()):
            os.makedirs(path())
        logging.basicConfig(filename=path() + datetime.datetime.now(
        ).strftime(logDateTimeFormat) + logFilesExtension, level=logging.DEBUG, format='%(asctime)s;%(levelname)s;%(message)s')
        cleanUp(max_logfiles)
    except Exception as E:
        logging.error(u'Logger exception: {0}'.format(str(E)))
        raise
