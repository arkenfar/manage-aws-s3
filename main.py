import logging
from s3 import gets3
from logger import logger

s3bucket = "backup-bucket-remove-later"
maxLogfiles = 10


def main(s3):
    try:
        logger(maxLogfiles)
        s3 = gets3(s3bucket)
        logging.info("Successfully got s3 " + s3)
    except Exception as E:
        logging.error(u'Exception: {0}'.format(str(E)))
        raise


if __name__ == '__main__':
    main(s3bucket)
