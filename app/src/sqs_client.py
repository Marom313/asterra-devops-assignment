import boto3
import os

def get_message():
    sqs = boto3.client("sqs")
    queue_url = os.getenv("SQS_URL")

    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1
    )

    if "Messages" not in response:
        return None

    body = response["Messages"][0]["Body"]
    return {"s3_key": body}
