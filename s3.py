import boto3

s3 = boto3.client('s3')


def getAllBuckets():
    try:
        response = s3.list_buckets()
        return response
    except Exception as E:
        raise
