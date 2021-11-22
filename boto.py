import boto3


def session(aws_access_key_id, aws_secret_access_key):
    try:
        boto_session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        if boto_session:
            return boto_session
    except Exception as err_session:
        raise err_session


# def getAllBuckets():
#     try:
#         response = s3.list_buckets()
#         logging.info(str(response))
#         buckets = response['Buckets']
#         logging.info("Successfully found a total of " +
#                      str(len(buckets)) + " s3 buckets")
#         return buckets
#     except Exception as E:
#         raise


def get_bucket(boto_session, s3_bucket):
    try:
        s3 = boto_session.resource('s3')
        bucket = s3.Bucket(s3_bucket)
        return bucket.name
    except Exception as err_get_bucket:
        raise err_get_bucket
