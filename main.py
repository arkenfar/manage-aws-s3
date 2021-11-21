import logging
from s3 import getAllBuckets
from logger import logger

s3bucket = "backup-bucket-remove-later"
maxLogfiles = 10


def main(s3):
    try:
        logger(maxLogfiles)
        response = getAllBuckets()
        buckets = []

        for bucket in response['Buckets']:
            bucketName = bucket["Name"]
            print(bucketName)
            buckets.append(bucketName)

        logging.info("Successfully found a total of " +
                     str(len(buckets)) + " s3 buckets")
    except Exception as E:
        logging.error(u'Exception: {0}'.format(str(E)))
        raise


if __name__ == '__main__':
    main(s3bucket)
