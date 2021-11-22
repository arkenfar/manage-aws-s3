import logging
import os
import yaml
from boto import get_bucket, session  # , getAllBuckets
from utils import ping, req
from logger import logger


def main():
    try:
        # .yml files
        try:
            # Read .yml Config file
            with open("config.yml", 'r', encoding='utf8') as stream:
                conf = yaml.safe_load(stream)
            # Read .yml Creds file
            with open("secrets.yml", 'r', encoding='utf8') as stream:
                secrets = yaml.safe_load(stream)
        except Exception as err_yml:
            print(err_yml)
            raise err_yml

        # Sett environment variables from config file
        os.environ["AWS_ACCESS_KEY_ID"] = secrets['AWS_ACCESS_KEY']
        os.environ["AWS_SECRET_ACCESS_KEY"] = secrets['AWS_SECRET_KEY']

        # Start logger
        logger(conf['MAX_LOGFILES'])

        # Boto session
        logging.debug(
            "Starting Boto session")
        botosession = session(os.environ["AWS_ACCESS_KEY_ID"],
                              os.environ["AWS_SECRET_ACCESS_KEY"])
        logging.debug(
            "Boto session successfully started")

        # Get s3 bucket
        logging.debug(
            "Getting bucket '%s'", secrets['S3_BUCKET'])
        bucket = str(get_bucket(botosession, secrets['S3_BUCKET']))
        logging.debug(
            "Successfully got s3 bucket '%s'", bucket)

        # Bucket https url
        bucket_url = 'https://' + bucket + '.s3.amazonaws.com'
        logging.debug(
            "Ping url '%s'", bucket_url)

        # Ping
        if not ping(bucket_url):
            logging.warning("'%s' is not responding to ping", bucket_url)
        else:
            logging.info("'%s' is responding to ping function", bucket_url)

        # Get request
        if not req(bucket_url):
            logging.warning(
                "'%s' does not return status code 200 or 403", bucket_url)
        else:
            logging.info(
                "GET request returned expected status code from url '%s'", bucket_url)

    # Main error handler
    except Exception as err_main:
        logging.error('Main exception: %s', str(err_main))
        raise


if __name__ == '__main__':
    main()
