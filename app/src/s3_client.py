import boto3
import os

def download_file(key):
    s3 = boto3.client("s3")
    bucket = os.getenv("S3_BUCKET")
    local_path = f"/tmp/{key}"
    s3.download_file(bucket, key, local_path)
    return local_path
