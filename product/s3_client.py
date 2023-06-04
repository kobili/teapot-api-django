import boto3
import logging
from uuid import uuid4
from botocore.exceptions import ClientError

from teapot_api.settings import S3_BUCKET

_s3_client = boto3.client(
    's3', 
    endpoint_url="https://0.0.0.0:4566",
    aws_access_key_id="localstack_placeholder",
    aws_secret_access_key="localstack_placeholder",
)

def create_s3_object(object_key: str):
    try:
        signed_url = _s3_client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": S3_BUCKET,
                "Key": object_key,
                "ContentType": "multipart/form-data",
            },
            ExpiresIn=600,
        )
    except ClientError as exc:
        logging.error(exc)

    return signed_url

def get_s3_object(object_key: str):
    try:
        signed_url = _s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": S3_BUCKET,
                "Key": object_key,
            },
            ExpiresIn=600,
        )
    except ClientError as exc:
        logging.error(exc)

    return signed_url
